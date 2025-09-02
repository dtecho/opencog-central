
#include <math.h>
#include <string.h>
#include "../include/llm_core.h"

// Scaled dot-product attention
void scaled_dot_product_attention(
    const float* queries,    // [seq_len, d_model]
    const float* keys,       // [seq_len, d_model] 
    const float* values,     // [seq_len, d_model]
    float* output,           // [seq_len, d_model]
    int seq_len,
    int d_model,
    float scale
) {
    // Compute Q * K^T
    float* scores = malloc(seq_len * seq_len * sizeof(float));
    
    for (int i = 0; i < seq_len; i++) {
        for (int j = 0; j < seq_len; j++) {
            float sum = 0.0f;
            for (int k = 0; k < d_model; k++) {
                sum += queries[i * d_model + k] * keys[j * d_model + k];
            }
            scores[i * seq_len + j] = sum * scale;
        }
    }
    
    // Apply softmax to each row
    for (int i = 0; i < seq_len; i++) {
        float max_val = scores[i * seq_len];
        for (int j = 1; j < seq_len; j++) {
            if (scores[i * seq_len + j] > max_val) {
                max_val = scores[i * seq_len + j];
            }
        }
        
        float sum = 0.0f;
        for (int j = 0; j < seq_len; j++) {
            scores[i * seq_len + j] = expf(scores[i * seq_len + j] - max_val);
            sum += scores[i * seq_len + j];
        }
        
        for (int j = 0; j < seq_len; j++) {
            scores[i * seq_len + j] /= sum;
        }
    }
    
    // Compute attention * values
    for (int i = 0; i < seq_len; i++) {
        for (int j = 0; j < d_model; j++) {
            float sum = 0.0f;
            for (int k = 0; k < seq_len; k++) {
                sum += scores[i * seq_len + k] * values[k * d_model + j];
            }
            output[i * d_model + j] = sum;
        }
    }
    
    free(scores);
}

// Multi-head attention
void multi_head_attention(
    const float* input,      // [seq_len, d_model]
    float* output,           // [seq_len, d_model]
    const float* wq,         // [d_model, d_model] query weights
    const float* wk,         // [d_model, d_model] key weights  
    const float* wv,         // [d_model, d_model] value weights
    const float* wo,         // [d_model, d_model] output weights
    int seq_len,
    int d_model,
    int num_heads
) {
    int head_dim = d_model / num_heads;
    float scale = 1.0f / sqrtf((float)head_dim);
    
    float* queries = malloc(seq_len * d_model * sizeof(float));
    float* keys = malloc(seq_len * d_model * sizeof(float));
    float* values = malloc(seq_len * d_model * sizeof(float));
    float* head_output = malloc(seq_len * d_model * sizeof(float));
    
    // Linear projections
    matrix_multiply(input, wq, queries, seq_len, d_model, d_model);
    matrix_multiply(input, wk, keys, seq_len, d_model, d_model);
    matrix_multiply(input, wv, values, seq_len, d_model, d_model);
    
    // Process each head
    for (int h = 0; h < num_heads; h++) {
        int offset = h * head_dim;
        
        scaled_dot_product_attention(
            queries + offset, 
            keys + offset,
            values + offset,
            head_output + offset,
            seq_len, head_dim, scale
        );
    }
    
    // Output projection
    matrix_multiply(head_output, wo, output, seq_len, d_model, d_model);
    
    free(queries);
    free(keys);
    free(values);
    free(head_output);
}
