
#include <stdint.h>
#include <math.h>
#include "../include/llm_core.h"

// INT8 quantization
void quantize_int8(const float* input, int8_t* output, float* scale, 
                   int size) {
    // Find min/max values
    float min_val = input[0];
    float max_val = input[0];
    
    for (int i = 1; i < size; i++) {
        if (input[i] < min_val) min_val = input[i];
        if (input[i] > max_val) max_val = input[i];
    }
    
    // Calculate scale
    float range = fmaxf(fabsf(min_val), fabsf(max_val));
    *scale = range / 127.0f;
    
    // Quantize
    for (int i = 0; i < size; i++) {
        float quantized = roundf(input[i] / *scale);
        output[i] = (int8_t)fmaxf(-128.0f, fminf(127.0f, quantized));
    }
}

void dequantize_int8(const int8_t* input, float* output, float scale, 
                     int size) {
    for (int i = 0; i < size; i++) {
        output[i] = (float)input[i] * scale;
    }
}

// INT4 quantization (packed)
void quantize_int4_packed(const float* input, uint8_t* output, float* scale,
                         int size) {
    // Find scale
    float max_val = 0.0f;
    for (int i = 0; i < size; i++) {
        max_val = fmaxf(max_val, fabsf(input[i]));
    }
    *scale = max_val / 7.0f;
    
    // Quantize and pack
    for (int i = 0; i < size; i += 2) {
        int8_t q1 = (int8_t)roundf(input[i] / *scale);
        q1 = fmaxf(-8, fminf(7, q1)) + 8; // Shift to 0-15 range
        
        int8_t q2 = 0;
        if (i + 1 < size) {
            q2 = (int8_t)roundf(input[i + 1] / *scale);
            q2 = fmaxf(-8, fminf(7, q2)) + 8;
        }
        
        output[i / 2] = (q1 & 0x0F) | ((q2 & 0x0F) << 4);
    }
}
