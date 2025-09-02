
#include <stdlib.h>
#include <string.h>
#include "../include/llm_core.h"

// Memory pool for efficient allocation
typedef struct {
    void* pool;
    size_t size;
    size_t used;
    size_t align;
} memory_pool_t;

memory_pool_t* create_memory_pool(size_t size) {
    memory_pool_t* pool = malloc(sizeof(memory_pool_t));
    if (!pool) return NULL;
    
    pool->pool = aligned_alloc(64, size); // 64-byte alignment for SIMD
    if (!pool->pool) {
        free(pool);
        return NULL;
    }
    
    pool->size = size;
    pool->used = 0;
    pool->align = 64;
    
    return pool;
}

void* pool_alloc(memory_pool_t* pool, size_t size) {
    if (!pool || pool->used + size > pool->size) {
        return NULL;
    }
    
    void* ptr = (char*)pool->pool + pool->used;
    pool->used += (size + pool->align - 1) & ~(pool->align - 1); // Align
    
    return ptr;
}

void destroy_memory_pool(memory_pool_t* pool) {
    if (pool) {
        free(pool->pool);
        free(pool);
    }
}

// CUDA memory management
#ifdef USE_CUDA
#include <cuda_runtime.h>

int cuda_malloc(void** ptr, size_t size) {
    cudaError_t err = cudaMalloc(ptr, size);
    return err == cudaSuccess ? 0 : -1;
}

int cuda_free(void* ptr) {
    cudaError_t err = cudaFree(ptr);
    return err == cudaSuccess ? 0 : -1;
}

int cuda_memcpy_h2d(void* dst, const void* src, size_t size) {
    cudaError_t err = cudaMemcpy(dst, src, size, cudaMemcpyHostToDevice);
    return err == cudaSuccess ? 0 : -1;
}

int cuda_memcpy_d2h(void* dst, const void* src, size_t size) {
    cudaError_t err = cudaMemcpy(dst, src, size, cudaMemcpyDeviceToHost);
    return err == cudaSuccess ? 0 : -1;
}
#endif
