
#include "llm_core.h"
#include <assert.h>
#include <string.h>

void test_str_lookup() {
    Tokenizer t;
    t.vocab_size = 3;
    t.vocab = malloc(3 * sizeof(char*));
    t.vocab[0] = "hello";
    t.vocab[1] = "world";
    t.vocab[2] = "test";
    
    assert(str_lookup("hello", &t) == 0);
    assert(str_lookup("world", &t) == 1);
    assert(str_lookup("test", &t) == 2);
    assert(str_lookup("notfound", &t) == -1);
    
    free(t.vocab);
    printf("String lookup test passed\n");
}

void test_safe_printf() {
    // This is mainly to test that it doesn't crash
    safe_printf("hello");
    safe_printf(NULL);
    safe_printf("");
    printf("\nSafe printf test passed\n");
}

int main() {
    test_str_lookup();
    test_safe_printf();
    printf("All tokenizer tests passed!\n");
    return 0;
}
