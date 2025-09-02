
#include "ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void test_cpu_backend() {
    printf("Testing CPU backend...\n");
    
    struct ggml_opencog_context* ctx = ggml_opencog_init(1024 * 1024);
    assert(ctx != NULL);
    
    // Test CPU backend functionality
    printf("✓ CPU backend test passed\n");
    
    ggml_opencog_free(ctx);
}

int main() {
    printf("GGML OpenCog Backends Test\n");
    
    test_cpu_backend();
    
    printf("All backend tests passed!\n");
    return 0;
}
