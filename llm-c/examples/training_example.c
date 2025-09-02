
#include <stdio.h>
#include <stdlib.h>
#include "../include/llm_core.h"

int main() {
    printf("LLM.C Training Example\n");
    
    // Model configuration
    transformer_config_t config = {
        .vocab_size = 50257,
        .d_model = 768,
        .n_layers = 12,
        .n_heads = 12,
        .seq_len = 1024,
        .d_ff = 3072,
        .dropout = 0.1f
    };
    
    // Calculate parameter count
    size_t param_count = calculate_weight_count(&config);
    printf("Model parameters: %zu\n", param_count);
    
    // Initialize weights randomly
    float* weights = malloc(param_count * sizeof(float));
    if (!weights) {
        fprintf(stderr, "Failed to allocate weights\n");
        return 1;
    }
    
    // Simple random initialization
    for (size_t i = 0; i < param_count; i++) {
        weights[i] = ((float)rand() / RAND_MAX - 0.5f) * 0.02f;
    }
    
    // Create optimizer
    adam_optimizer_t* optimizer = create_adam_optimizer(
        param_count, 0.0001f, 0.9f, 0.999f, 1e-8f
    );
    
    if (!optimizer) {
        fprintf(stderr, "Failed to create optimizer\n");
        free(weights);
        return 1;
    }
    
    // Training loop (simplified)
    int batch_size = 4;
    int seq_len = 512;
    
    int* input_ids = malloc(batch_size * seq_len * sizeof(int));
    float* output = malloc(batch_size * seq_len * config.vocab_size * sizeof(float));
    float* gradients = malloc(param_count * sizeof(float));
    
    for (int epoch = 0; epoch < 10; epoch++) {
        // Generate dummy training data
        for (int i = 0; i < batch_size * seq_len; i++) {
            input_ids[i] = rand() % config.vocab_size;
        }
        
        // Forward pass
        int result = transformer_forward(&config, weights, input_ids, output,
                                       batch_size, seq_len);
        
        if (result != 0) {
            fprintf(stderr, "Forward pass failed\n");
            break;
        }
        
        // Dummy gradient computation (would compute actual gradients in real training)
        for (size_t i = 0; i < param_count; i++) {
            gradients[i] = ((float)rand() / RAND_MAX - 0.5f) * 0.001f;
        }
        
        // Optimizer step
        adam_step(optimizer, weights, gradients, param_count);
        
        printf("Epoch %d completed\n", epoch + 1);
    }
    
    // Save trained model
    if (save_model("model.bin", &config, weights, param_count) == 0) {
        printf("Model saved successfully\n");
    } else {
        printf("Failed to save model\n");
    }
    
    // Cleanup
    free(input_ids);
    free(output);
    free(gradients);
    free(weights);
    destroy_adam_optimizer(optimizer);
    
    return 0;
}
