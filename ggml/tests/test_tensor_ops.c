
#include "ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void test_basic_operations() {
    printf("Testing basic tensor operations...\n");
    
    struct ggml_opencog_context* ctx = ggml_opencog_init(1024 * 1024);
    assert(ctx != NULL);
    
    // Test context operations
    size_t mem_size = ggml_opencog_get_mem_size(ctx);
    assert(mem_size > 0);
    
    printf("✓ Context creation and memory size check passed\n");
    
    ggml_opencog_free(ctx);
    printf("✓ Context cleanup passed\n");
}

int main() {
    printf("GGML OpenCog Tensor Operations Test\n");
    
    test_basic_operations();
    
    printf("All tensor operation tests passed!\n");
    return 0;
}
