
#include "ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    printf("GGML OpenCog GPT-2 Inference Example\n");
    
    // Initialize GGML OpenCog context
    struct ggml_opencog_context* ctx = ggml_opencog_init(1024 * 1024); // 1MB
    if (!ctx) {
        fprintf(stderr, "Failed to initialize GGML OpenCog context\n");
        return 1;
    }
    
    printf("GGML OpenCog context initialized successfully\n");
    printf("Context memory size: %zu bytes\n", ggml_opencog_get_mem_size(ctx));
    
    // Cleanup
    ggml_opencog_free(ctx);
    printf("Context freed\n");
    
    return 0;
}
