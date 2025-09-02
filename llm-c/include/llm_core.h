#ifndef LLM_CORE_H
#define LLM_CORE_H

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <math.h>

#ifdef __cplusplus
extern "C" {
#endif

// Configuration structure
typedef struct {
    int vocab_size;
    int seq_len;
    int dim;
    int n_layers;
    int n_heads;
    int n_kv_heads;
    int hidden_dim;
    bool shared_weights;
} Config;

// Transformer weights
typedef struct {
    float* token_embedding_table;
    float* rms_att_weight;
    float* wq;
    float* wk;
    float* wv;
    float* wo;
    float* rms_ffn_weight;
    float* w1;
    float* w2;
    float* w3;
    float* rms_final_weight;
    float* freq_cis_real;
    float* freq_cis_imag;
    float* wcls;
} TransformerWeights;

// Transformer state
typedef struct {
    float* x;
    float* xb;
    float* xb2;
    float* hb;
    float* hb2;
    float* q;
    float* k;
    float* v;
    float* att;
    float* logits;
    float* key_cache;
    float* value_cache;
} RunState;

// Main transformer structure
typedef struct {
    Config config;
    TransformerWeights weights;
    RunState state;
    int fd;
    float* data;
    ssize_t file_size;
} Transformer;

// Core functions
int transformer_init(Transformer* t, char* checkpoint_path);
void transformer_free(Transformer* t);
float* forward(Transformer* t, int token, int pos);
void rmsnorm(float* o, float* x, float* weight, int size);
void softmax(float* x, int size);
void matmul(float* xout, float* x, float* w, int n, int d);

// Sampling functions
int sample_argmax(float* probabilities, int n);
int sample_mult(float* probabilities, int n, float coin);
int sample_topp(float* probabilities, int n, float topp, float* probabilities_sorted, int* indices);

// Tokenizer functions
typedef struct {
    char** vocab;
    float* vocab_scores;
    int vocab_size;
    unsigned int max_token_length;
    unsigned char byte_pieces[512];
} Tokenizer;

int tokenizer_init(Tokenizer* t, char* tokenizer_path, int vocab_size);
void tokenizer_free(Tokenizer* t);
char* decode(Tokenizer* t, int prev_token, int token);
void safe_printf(char* piece);
int str_lookup(char* str, Tokenizer* t);
void bpe_encode(char* text, Tokenizer* t, int* tokens, int* n_tokens);

// Generation function
void generate(Transformer* transformer, Tokenizer* tokenizer, char* prompt, int steps);

#ifdef __cplusplus
}
#endif

#endif // LLM_CORE_H
#ifndef LLM_CORE_H
#define LLM_CORE_H

#include <stdint.h>
#include <stddef.h>

// Forward declarations
typedef struct transformer_config transformer_config_t;
typedef struct memory_pool memory_pool_t;
typedef struct adam_optimizer adam_optimizer_t;

// Configuration structure
struct transformer_config {
    int vocab_size;
    int d_model;
    int n_layers;
    int n_heads;
    int seq_len;
    int d_ff;
    float dropout;
};

// Core transformer functions
int transformer_forward(const transformer_config_t* config, 
                       const float* weights,
                       const int* input_ids,
                       float* output,
                       int batch_size,
                       int seq_len);

// Memory management
memory_pool_t* create_memory_pool(size_t size);
void* pool_alloc(memory_pool_t* pool, size_t size);
void destroy_memory_pool(memory_pool_t* pool);

#ifdef USE_CUDA
int cuda_malloc(void** ptr, size_t size);
int cuda_free(void* ptr);
int cuda_memcpy_h2d(void* dst, const void* src, size_t size);
int cuda_memcpy_d2h(void* dst, const void* src, size_t size);
#endif

// Attention mechanisms
void scaled_dot_product_attention(const float* queries, const float* keys,
                                 const float* values, float* output,
                                 int seq_len, int d_model, float scale);

void multi_head_attention(const float* input, float* output,
                         const float* wq, const float* wk, const float* wv,
                         const float* wo, int seq_len, int d_model, int num_heads);

// Activation functions
void relu(const float* input, float* output, int size);
void gelu(const float* input, float* output, int size);
void swish(const float* input, float* output, int size);
void softmax(const float* input, float* output, int size);
void layer_norm(const float* input, float* output, const float* gamma,
                const float* beta, int size, float eps);

// Optimization
adam_optimizer_t* create_adam_optimizer(int param_count, float lr,
                                       float beta1, float beta2, float eps);
void adam_step(adam_optimizer_t* opt, float* params, const float* gradients,
               int param_count);
void destroy_adam_optimizer(adam_optimizer_t* opt);

// Model I/O
int save_model(const char* filename, const transformer_config_t* config,
               const float* weights, size_t weight_count);
int load_model(const char* filename, transformer_config_t* config,
               float** weights, size_t* weight_count);
size_t calculate_weight_count(const transformer_config_t* config);

// Quantization
void quantize_int8(const float* input, int8_t* output, float* scale, int size);
void dequantize_int8(const int8_t* input, float* output, float scale, int size);
void quantize_int4_packed(const float* input, uint8_t* output, float* scale, int size);

// Tokenization
typedef struct tokenizer tokenizer_t;

tokenizer_t* create_tokenizer(const char* vocab_file);
int tokenize(tokenizer_t* tok, const char* text, int* tokens, int max_tokens);
char* detokenize(tokenizer_t* tok, const int* tokens, int num_tokens);
void destroy_tokenizer(tokenizer_t* tok);

// Sampling
int sample_token(const float* logits, int vocab_size, float temperature, float top_p);
void generate_text(const transformer_config_t* config, const float* weights,
                   tokenizer_t* tokenizer, const char* prompt, char* output,
                   int max_tokens, float temperature, float top_p);

// Utility functions
void matrix_multiply(const float* a, const float* b, float* c, 
                    int m, int n, int k);

// Function declarations for optimization algorithms
void adam_optimizer_step(float* params, float* gradients, float* m, float* v, 
                        int size, float lr, float beta1, float beta2, float epsilon, int step);
void sgd_optimizer_step(float* params, float* gradients, int size, float lr, float momentum);

// OpenCog-specific functionality
typedef struct AtomSpace AtomSpace;
typedef struct AttentionBank AttentionBank;
typedef struct SchemeEnvironment SchemeEnvironment;
typedef struct PatternMiner PatternMiner;
typedef struct Population Population;

// AtomSpace bridge functions
AtomSpace* create_atomspace(size_t initial_capacity);
void add_concept_node(AtomSpace* space, const char* name, float truth, float conf);
void add_predicate_node(AtomSpace* space, const char* name, float truth, float conf);
void cleanup_atomspace(AtomSpace* space);

// ECAN attention functions
AttentionBank* create_attention_bank(size_t capacity);
void update_attention(AttentionBank* bank, const char* atom_id, float activity);
void manage_attention_economy(AttentionBank* bank);

// Scheme interface functions
SchemeEnvironment* create_scheme_env(size_t capacity);
char* eval_scheme(SchemeEnvironment* env, const char* expression);
int load_scheme_file(SchemeEnvironment* env, const char* filename);
void cleanup_scheme_env(SchemeEnvironment* env);

// Pattern mining functions
PatternMiner* create_pattern_miner(size_t capacity, int min_freq, float min_sig);
void mine_patterns(PatternMiner* miner, char** corpus, int corpus_size);
void cleanup_pattern_miner(PatternMiner* miner);

// MOSES evolution functions
Population* create_population(size_t max_size);
void run_moses_evolution(Population* pop, struct {int max_generations; float mutation_rate; float crossover_rate; int population_size; int elitism_count;} config, float** training_data, int data_size);
void cleanup_population(Population* pop);

#endif // LLM_CORE_H