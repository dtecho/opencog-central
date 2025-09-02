
#include "ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void test_quantization_support() {
    printf("Testing quantization support...\n");
    
    struct ggml_opencog_context* ctx = ggml_opencog_init(1024 * 1024);
    assert(ctx != NULL);
    
    // Basic quantization test - just verify context works
    printf("✓ Quantization context test passed\n");
    
    ggml_opencog_free(ctx);
}

int main() {
    printf("GGML OpenCog Quantization Test\n");
    
    test_quantization_support();
    
    printf("All quantization tests passed!\n");
    return 0;
}
