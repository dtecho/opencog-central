
#include <math.h>
#include "../include/llm_core.h"

void relu(const float* input, float* output, int size) {
    for (int i = 0; i < size; i++) {
        output[i] = fmaxf(0.0f, input[i]);
    }
}

void gelu(const float* input, float* output, int size) {
    const float sqrt_2_pi = sqrtf(2.0f / M_PI);
    
    for (int i = 0; i < size; i++) {
        float x = input[i];
        float tanh_arg = sqrt_2_pi * (x + 0.044715f * x * x * x);
        output[i] = 0.5f * x * (1.0f + tanhf(tanh_arg));
    }
}

void swish(const float* input, float* output, int size) {
    for (int i = 0; i < size; i++) {
        float x = input[i];
        output[i] = x / (1.0f + expf(-x));
    }
}

void softmax(const float* input, float* output, int size) {
    // Find maximum for numerical stability
    float max_val = input[0];
    for (int i = 1; i < size; i++) {
        if (input[i] > max_val) {
            max_val = input[i];
        }
    }
    
    // Compute exponentials and sum
    float sum = 0.0f;
    for (int i = 0; i < size; i++) {
        output[i] = expf(input[i] - max_val);
        sum += output[i];
    }
    
    // Normalize
    for (int i = 0; i < size; i++) {
        output[i] /= sum;
    }
}

void layer_norm(const float* input, float* output, const float* gamma, 
                const float* beta, int size, float eps) {
    // Compute mean
    float mean = 0.0f;
    for (int i = 0; i < size; i++) {
        mean += input[i];
    }
    mean /= size;
    
    // Compute variance
    float variance = 0.0f;
    for (int i = 0; i < size; i++) {
        float diff = input[i] - mean;
        variance += diff * diff;
    }
    variance /= size;
    
    // Normalize and apply scale/shift
    float inv_std = 1.0f / sqrtf(variance + eps);
    for (int i = 0; i < size; i++) {
        output[i] = gamma[i] * (input[i] - mean) * inv_std + beta[i];
    }
}
