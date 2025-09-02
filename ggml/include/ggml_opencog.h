
#ifndef GGML_OPENCOG_H
#define GGML_OPENCOG_H

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

// GGML OpenCog API Version
#define GGML_OPENCOG_VERSION_MAJOR 1
#define GGML_OPENCOG_VERSION_MINOR 0
#define GGML_OPENCOG_VERSION_PATCH 0

// Forward declarations
struct ggml_context;
struct ggml_tensor;
struct ggml_cgraph;

// Context management
struct ggml_context* ggml_opencog_init(size_t mem_size);
void ggml_opencog_free(struct ggml_context* ctx);

// Tensor operations
struct ggml_tensor* ggml_opencog_new_tensor_1d(
    struct ggml_context* ctx,
    enum ggml_type type,
    int64_t ne0);

struct ggml_tensor* ggml_opencog_new_tensor_2d(
    struct ggml_context* ctx,
    enum ggml_type type,
    int64_t ne0,
    int64_t ne1);

// Computation graph
struct ggml_cgraph* ggml_opencog_new_graph(struct ggml_context* ctx);
void ggml_opencog_graph_compute(struct ggml_cgraph* cgraph);

// Quantization support
bool ggml_opencog_quantize_q4_0(const float* src, void* dst, int n);
bool ggml_opencog_quantize_q4_1(const float* src, void* dst, int n);
bool ggml_opencog_quantize_q8_0(const float* src, void* dst, int n);

// Backend enumeration
enum ggml_opencog_backend {
    GGML_OPENCOG_BACKEND_CPU,
    GGML_OPENCOG_BACKEND_CUDA,
    GGML_OPENCOG_BACKEND_METAL,
    GGML_OPENCOG_BACKEND_OPENCL,
    GGML_OPENCOG_BACKEND_SYCL
};

// Backend management
bool ggml_opencog_backend_supported(enum ggml_opencog_backend backend);
void ggml_opencog_backend_set_default(enum ggml_opencog_backend backend);

#ifdef __cplusplus
}
#endif

#endif // GGML_OPENCOG_H
