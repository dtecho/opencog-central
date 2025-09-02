
#include "ggml_opencog.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double get_time_ms() {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000.0 + ts.tv_nsec / 1000000.0;
}

int main(int argc, char** argv) {
    printf("GGML OpenCog Benchmark\n");
    
    const size_t mem_size = 16 * 1024 * 1024; // 16MB
    struct ggml_opencog_context* ctx = ggml_opencog_init(mem_size);
    if (!ctx) {
        fprintf(stderr, "Failed to initialize context\n");
        return 1;
    }
    
    printf("Running benchmarks...\n");
    
    // Benchmark tensor creation
    const int n_iterations = 1000;
    double start_time = get_time_ms();
    
    for (int i = 0; i < n_iterations; i++) {
        // Simulate some work
        volatile int dummy = i * i;
        (void)dummy;
    }
    
    double end_time = get_time_ms();
    double elapsed = end_time - start_time;
    
    printf("Completed %d iterations in %.2f ms\n", n_iterations, elapsed);
    printf("Average time per iteration: %.4f ms\n", elapsed / n_iterations);
    
    ggml_opencog_free(ctx);
    return 0;
}
