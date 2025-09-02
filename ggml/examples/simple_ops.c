
#include "../include/ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("GGML OpenCog Simple Operations Example\n");
    
    // Initialize context with 1MB memory
    struct ggml_context* ctx = ggml_opencog_init(1024 * 1024);
    if (!ctx) {
        printf("Failed to initialize GGML context\n");
        return 1;
    }
    
    printf("✓ Initialized GGML context\n");
    
    // Create 1D tensor
    struct ggml_tensor* tensor_1d = ggml_opencog_new_tensor_1d(ctx, GGML_TYPE_F32, 128);
    if (tensor_1d) {
        printf("✓ Created 1D tensor with 128 elements\n");
    }
    
    // Create 2D tensor
    struct ggml_tensor* tensor_2d = ggml_opencog_new_tensor_2d(ctx, GGML_TYPE_F32, 64, 32);
    if (tensor_2d) {
        printf("✓ Created 2D tensor with dimensions 64x32\n");
    }
    
    // Create computation graph
    struct ggml_cgraph* graph = ggml_opencog_new_graph(ctx);
    if (graph) {
        printf("✓ Created computation graph\n");
    }
    
    // Check backend support
    printf("Backend support:\n");
    printf("  CPU: %s\n", ggml_opencog_backend_supported(GGML_OPENCOG_BACKEND_CPU) ? "Yes" : "No");
    printf("  CUDA: %s\n", ggml_opencog_backend_supported(GGML_OPENCOG_BACKEND_CUDA) ? "Yes" : "No");
    printf("  Metal: %s\n", ggml_opencog_backend_supported(GGML_OPENCOG_BACKEND_METAL) ? "Yes" : "No");
    
    // Cleanup
    ggml_opencog_free(ctx);
    printf("✓ Cleaned up resources\n");
    
    printf("Example completed successfully!\n");
    return 0;
}
