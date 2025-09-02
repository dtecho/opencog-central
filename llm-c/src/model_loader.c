
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../include/llm_core.h"

typedef struct {
    char magic[4];     // "LLM1"
    uint32_t version;
    uint32_t vocab_size;
    uint32_t d_model;
    uint32_t n_layers;
    uint32_t n_heads;
    uint32_t seq_len;
    uint32_t checksum;
} model_header_t;

int save_model(const char* filename, const transformer_config_t* config,
               const float* weights, size_t weight_count) {
    FILE* file = fopen(filename, "wb");
    if (!file) return -1;
    
    model_header_t header = {
        .magic = {'L', 'L', 'M', '1'},
        .version = 1,
        .vocab_size = config->vocab_size,
        .d_model = config->d_model,
        .n_layers = config->n_layers,
        .n_heads = config->n_heads,
        .seq_len = config->seq_len,
        .checksum = 0 // TODO: implement checksum
    };
    
    // Write header
    if (fwrite(&header, sizeof(header), 1, file) != 1) {
        fclose(file);
        return -1;
    }
    
    // Write weights
    if (fwrite(weights, sizeof(float), weight_count, file) != weight_count) {
        fclose(file);
        return -1;
    }
    
    fclose(file);
    return 0;
}

int load_model(const char* filename, transformer_config_t* config,
               float** weights, size_t* weight_count) {
    FILE* file = fopen(filename, "rb");
    if (!file) return -1;
    
    model_header_t header;
    if (fread(&header, sizeof(header), 1, file) != 1) {
        fclose(file);
        return -1;
    }
    
    // Verify magic number
    if (memcmp(header.magic, "LLM1", 4) != 0) {
        fclose(file);
        return -1;
    }
    
    // Set config
    config->vocab_size = header.vocab_size;
    config->d_model = header.d_model;
    config->n_layers = header.n_layers;
    config->n_heads = header.n_heads;
    config->seq_len = header.seq_len;
    
    // Calculate weight count
    *weight_count = calculate_weight_count(config);
    
    // Allocate and read weights
    *weights = malloc(*weight_count * sizeof(float));
    if (!*weights) {
        fclose(file);
        return -1;
    }
    
    if (fread(*weights, sizeof(float), *weight_count, file) != *weight_count) {
        free(*weights);
        *weights = NULL;
        fclose(file);
        return -1;
    }
    
    fclose(file);
    return 0;
}

size_t calculate_weight_count(const transformer_config_t* config) {
    size_t count = 0;
    
    // Embedding weights
    count += config->vocab_size * config->d_model;
    count += config->seq_len * config->d_model; // positional embeddings
    
    // Transformer layers
    for (int i = 0; i < config->n_layers; i++) {
        // Multi-head attention
        count += 4 * config->d_model * config->d_model; // Q, K, V, O projections
        
        // Feed-forward network
        count += config->d_model * (4 * config->d_model); // up projection
        count += (4 * config->d_model) * config->d_model; // down projection
        
        // Layer norm parameters
        count += 2 * config->d_model; // attention layer norm
        count += 2 * config->d_model; // ffn layer norm
    }
    
    // Final layer norm and output projection
    count += 2 * config->d_model; // final layer norm
    count += config->d_model * config->vocab_size; // output projection
    
    return count;
}
