
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../include/llm_core.h"

double get_time_ms() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000.0 + ts.tv_nsec / 1000000.0;
}

void benchmark_attention(int seq_len, int d_model, int num_iterations) {
    printf("\nBenchmarking attention mechanism...\n");
    printf("Sequence length: %d, Model dimension: %d\n", seq_len, d_model);
    
    // Allocate test data
    float* queries = malloc(seq_len * d_model * sizeof(float));
    float* keys = malloc(seq_len * d_model * sizeof(float));
    float* values = malloc(seq_len * d_model * sizeof(float));
    float* output = malloc(seq_len * d_model * sizeof(float));
    
    // Initialize with random data
    for (int i = 0; i < seq_len * d_model; i++) {
        queries[i] = (float)rand() / RAND_MAX;
        keys[i] = (float)rand() / RAND_MAX;
        values[i] = (float)rand() / RAND_MAX;
    }
    
    double start_time = get_time_ms();
    
    for (int i = 0; i < num_iterations; i++) {
        scaled_dot_product_attention(queries, keys, values, output,
                                   seq_len, d_model, 1.0f / sqrtf(d_model));
    }
    
    double end_time = get_time_ms();
    double avg_time = (end_time - start_time) / num_iterations;
    
    printf("Average attention time: %.2f ms\n", avg_time);
    printf("Throughput: %.2f tokens/second\n", seq_len * 1000.0 / avg_time);
    
    free(queries);
    free(keys);
    free(values);
    free(output);
}

void benchmark_transformer(const transformer_config_t* config, int num_iterations) {
    printf("\nBenchmarking full transformer forward pass...\n");
    
    size_t weight_count = calculate_weight_count(config);
    float* weights = malloc(weight_count * sizeof(float));
    int* input_ids = malloc(config->seq_len * sizeof(int));
    float* output = malloc(config->seq_len * config->vocab_size * sizeof(float));
    
    // Initialize with random data
    for (size_t i = 0; i < weight_count; i++) {
        weights[i] = (float)rand() / RAND_MAX;
    }
    
    for (int i = 0; i < config->seq_len; i++) {
        input_ids[i] = rand() % config->vocab_size;
    }
    
    double start_time = get_time_ms();
    
    for (int i = 0; i < num_iterations; i++) {
        transformer_forward(config, weights, input_ids, output, 1, config->seq_len);
    }
    
    double end_time = get_time_ms();
    double avg_time = (end_time - start_time) / num_iterations;
    
    printf("Average forward pass time: %.2f ms\n", avg_time);
    printf("Parameters: %zu (%.1f MB)\n", weight_count, weight_count * 4.0 / 1024 / 1024);
    
    free(weights);
    free(input_ids);
    free(output);
}

int main() {
    printf("LLM.C Performance Benchmarks\n");
    printf("=============================\n");
    
    // Benchmark attention at different scales
    benchmark_attention(128, 768, 100);
    benchmark_attention(512, 768, 50);
    benchmark_attention(1024, 768, 10);
    
    // Benchmark different model sizes
    transformer_config_t small_config = {
        .vocab_size = 50257,
        .d_model = 768,
        .n_layers = 12,
        .n_heads = 12,
        .seq_len = 1024,
        .d_ff = 3072,
        .dropout = 0.1f
    };
    
    transformer_config_t large_config = {
        .vocab_size = 50257,
        .d_model = 1536,
        .n_layers = 24,
        .n_heads = 24,
        .seq_len = 1024,
        .d_ff = 6144,
        .dropout = 0.1f
    };
    
    benchmark_transformer(&small_config, 10);
    benchmark_transformer(&large_config, 5);
    
    return 0;
}
