
#include "llm_core.h"
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>

void rmsnorm(float* o, float* x, float* weight, int size) {
    // Calculate sum of squares
    float ss = 0.0f;
    for (int j = 0; j < size; j++) {
        ss += x[j] * x[j];
    }
    ss /= size;
    ss += 1e-5f;
    ss = 1.0f / sqrtf(ss);
    // Normalize and scale
    for (int j = 0; j < size; j++) {
        o[j] = weight[j] * (ss * x[j]);
    }
}

void softmax(float* x, int size) {
    // Find max value (for numerical stability)
    float max_val = x[0];
    for (int i = 1; i < size; i++) {
        if (x[i] > max_val) {
            max_val = x[i];
        }
    }
    // Exp and sum
    float sum = 0.0f;
    for (int i = 0; i < size; i++) {
        x[i] = expf(x[i] - max_val);
        sum += x[i];
    }
    // Normalize
    for (int i = 0; i < size; i++) {
        x[i] /= sum;
    }
}

void matmul(float* xout, float* x, float* w, int n, int d) {
    // W (d,n) @ x (n,) -> xout (d,)
    for (int i = 0; i < d; i++) {
        float val = 0.0f;
        for (int j = 0; j < n; j++) {
            val += w[i * n + j] * x[j];
        }
        xout[i] = val;
    }
}

float* forward(Transformer* t, int token, int pos) {
    Config* p = &t->config;
    TransformerWeights* w = &t->weights;
    RunState* s = &t->state;
    float *x = s->x;
    int dim = p->dim;
    int kv_dim = (p->dim * p->n_kv_heads) / p->n_heads;
    int kv_mul = p->n_heads / p->n_kv_heads; // integer multiplier of the kv sharing in multiquery
    int hidden_dim = p->hidden_dim;
    int head_size = dim / p->n_heads;

    // Copy the token embedding into x
    float* content_row = w->token_embedding_table + token * dim;
    for (int i = 0; i < dim; i++) {
        x[i] = content_row[i];
    }

    // Forward all the layers
    for (int l = 0; l < p->n_layers; l++) {

        // Attention rmsnorm
        rmsnorm(s->xb, x, w->rms_att_weight + l*dim, dim);

        // Key and value point to the kv cache
        int loff = l * p->seq_len * kv_dim; // kv cache layer offset for convenience
        s->k = s->key_cache + loff + pos * kv_dim;
        s->v = s->value_cache + loff + pos * kv_dim;

        // QKV matmuls for this position
        matmul(s->q, s->xb, w->wq + l*dim*dim, dim, dim);
        matmul(s->k, s->xb, w->wk + l*dim*kv_dim, dim, kv_dim);
        matmul(s->v, s->xb, w->wv + l*dim*kv_dim, dim, kv_dim);

        // RoPE relative positional encoding: complex-valued rotate q and k in each head
        for (int i = 0; i < dim; i+=2) {
            int head_dim = i % head_size;
            float freq = 1.0f / powf(10000.0f, head_dim / (float)head_size);
            float val = pos * freq;
            float fcr = cosf(val);
            float fci = sinf(val);
            int rotn = i < kv_dim ? 2 : 1; // how many vectors? 2 = q & k, 1 = q only
            for (int v = 0; v < rotn; v++) {
                float* vec = v == 0 ? s->q : s->k; // the vector to rotate (query or key)
                float v0 = vec[i];
                float v1 = vec[i+1];
                vec[i]   = v0 * fcr - v1 * fci;
                vec[i+1] = v0 * fci + v1 * fcr;
            }
        }

        // Multihead attention. Iterate over all heads
        for (int h = 0; h < p->n_heads; h++) {
            // Get the query vector for this head
            float* q = s->q + h * head_size;
            // Attention scores for this head
            float* att = s->att + h * p->seq_len;
            // Iterate over all timesteps, including the current one
            for (int t = 0; t <= pos; t++) {
                // Get the key vector for this head and at this timestep
                float* k = s->key_cache + loff + t * kv_dim + (h / kv_mul) * head_size;
                // Calculate the attention score as the dot product of q and k
                float score = 0.0f;
                for (int i = 0; i < head_size; i++) {
                    score += q[i] * k[i];
                }
                score /= sqrtf(head_size);
                // Save the score to the attention buffer
                att[t] = score;
            }

            // Softmax the scores to get attention weights
            softmax(att, pos + 1);

            // Weighted sum of the values, store back into xb
            float* xb = s->xb + h * head_size;
            for (int i = 0; i < head_size; i++) {
                xb[i] = 0.0f;
            }
            for (int t = 0; t <= pos; t++) {
                // Get the value vector for this head and at this timestep
                float* v = s->value_cache + loff + t * kv_dim + (h / kv_mul) * head_size;
                // Get the attention weight for this timestep
                float a = att[t];
                // Accumulate the weighted value into xb
                for (int i = 0; i < head_size; i++) {
                    xb[i] += a * v[i];
                }
            }
        }

        // Final matmul to get the output of the attention
        matmul(s->xb2, s->xb, w->wo + l*dim*dim, dim, dim);

        // Residual connection back into x
        for (int i = 0; i < dim; i++) {
            x[i] += s->xb2[i];
        }

        // FFN rmsnorm
        rmsnorm(s->xb, x, w->rms_ffn_weight + l*dim, dim);

        // Now for FFN in PyTorch we have: self.w2(F.silu(self.w1(x)) * self.w3(x))
        // First calculate self.w1(x) and self.w3(x)
        matmul(s->hb, s->xb, w->w1 + l*dim*hidden_dim, dim, hidden_dim);
        matmul(s->hb2, s->xb, w->w3 + l*dim*hidden_dim, dim, hidden_dim);

        // SwiGLU non-linearity
        for (int i = 0; i < hidden_dim; i++) {
            float val = s->hb[i];
            // silu(x)=x*σ(x), where σ(x)=1/(1+e^(-x))
            val *= (1.0f / (1.0f + expf(-val)));
            val *= s->hb2[i];
            s->hb[i] = val;
        }

        // Final matmul to get the output of the ffn
        matmul(s->xb, s->hb, w->w2 + l*dim*hidden_dim, hidden_dim, dim);

        // Residual connection
        for (int i = 0; i < dim; i++) {
            x[i] += s->xb[i];
        }
    }

    // Final rmsnorm
    rmsnorm(x, x, w->rms_final_weight, dim);

    // Classifier into logits
    matmul(s->logits, x, w->wcls, p->dim, p->vocab_size);
    return s->logits;
}

int transformer_init(Transformer* t, char* checkpoint_path) {
    FILE* file = fopen(checkpoint_path, "rb");
    if (!file) {
        fprintf(stderr, "Couldn't open file %s\n", checkpoint_path);
        return 1;
    }
    // Read in the config header
    if (fread(&t->config, sizeof(Config), 1, file) != 1) {
        return 1;
    }
    // Negative vocab size is hacky way of signaling unshared weights. Bit yikes.
    int shared_weights = t->config.vocab_size > 0 ? 1 : 0;
    t->config.vocab_size = abs(t->config.vocab_size);

    // Figure out the file size
    fseek(file, 0, SEEK_END); // move file pointer to end of file
    t->file_size = ftell(file); // get the file size, in bytes
    fclose(file);
    // Memory map the Transformer weights into the data pointer
    t->fd = open(checkpoint_path, O_RDONLY); // open in read only mode
    if (t->fd == -1) {
        fprintf(stderr, "open failed!\n");
        return 1;
    }
    t->data = mmap(NULL, t->file_size, PROT_READ, MAP_PRIVATE, t->fd, 0);
    if (t->data == MAP_FAILED) {
        fprintf(stderr, "mmap failed!\n");
        return 1;
    }
    float* weights_ptr = t->data + sizeof(Config)/sizeof(float);

    Config* p = &t->config;
    int head_size = p->dim / p->n_heads;
    unsigned long long n_layers = p->n_layers;
    t->weights.token_embedding_table = weights_ptr;
    weights_ptr += p->vocab_size * p->dim;
    t->weights.rms_att_weight = weights_ptr;
    weights_ptr += n_layers * p->dim;
    t->weights.wq = weights_ptr;
    weights_ptr += n_layers * p->dim * (p->n_heads * head_size);
    t->weights.wk = weights_ptr;
    weights_ptr += n_layers * p->dim * (p->n_kv_heads * head_size);
    t->weights.wv = weights_ptr;
    weights_ptr += n_layers * p->dim * (p->n_kv_heads * head_size);
    t->weights.wo = weights_ptr;
    weights_ptr += n_layers * (p->n_heads * head_size) * p->dim;
    t->weights.rms_ffn_weight = weights_ptr;
    weights_ptr += n_layers * p->dim;
    t->weights.w1 = weights_ptr;
    weights_ptr += n_layers * p->dim * p->hidden_dim;
    t->weights.w2 = weights_ptr;
    weights_ptr += n_layers * p->hidden_dim * p->dim;
    t->weights.w3 = weights_ptr;
    weights_ptr += n_layers * p->dim * p->hidden_dim;
    t->weights.rms_final_weight = weights_ptr;
    weights_ptr += p->dim;
    weights_ptr += p->seq_len * head_size / 2; // skip what used to be freq_cis_real
    weights_ptr += p->seq_len * head_size / 2; // skip what used to be freq_cis_imag
    t->weights.wcls = shared_weights ? t->weights.token_embedding_table : weights_ptr;

    // malloc run state
    int kv_dim = (p->dim * p->n_kv_heads) / p->n_heads;
    t->state.x = calloc(p->dim, sizeof(float));
    t->state.xb = calloc(p->dim, sizeof(float));
    t->state.xb2 = calloc(p->dim, sizeof(float));
    t->state.hb = calloc(p->hidden_dim, sizeof(float));
    t->state.hb2 = calloc(p->hidden_dim, sizeof(float));
    t->state.q = calloc(p->dim, sizeof(float));
    t->state.key_cache = calloc(p->n_layers * p->seq_len * kv_dim, sizeof(float));
    t->state.value_cache = calloc(p->n_layers * p->seq_len * kv_dim, sizeof(float));
    t->state.att = calloc(p->n_heads * p->seq_len, sizeof(float));
    t->state.logits = calloc(p->vocab_size, sizeof(float));
    
    // Ensure all mallocs went fine
    if (!t->state.x || !t->state.xb || !t->state.xb2 || !t->state.hb || !t->state.hb2 ||
        !t->state.q || !t->state.key_cache || !t->state.value_cache || !t->state.att || !t->state.logits) {
        fprintf(stderr, "malloc failed!\n");
        return 1;
    }
    return 0;
}

void transformer_free(Transformer* t) {
    if (t->data != MAP_FAILED) {
        munmap(t->data, t->file_size);
    }
    if (t->fd != -1) {
        close(t->fd);
    }
    free(t->state.x);
    free(t->state.xb);
    free(t->state.xb2);
    free(t->state.hb);
    free(t->state.hb2);
    free(t->state.q);
    free(t->state.att);
    free(t->state.logits);
    free(t->state.key_cache);
    free(t->state.value_cache);
}
