
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
