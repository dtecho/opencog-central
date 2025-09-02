
# GGML Examples

# Simple tensor operations example
add_executable(simple_ops simple_ops.c)
target_link_libraries(simple_ops ggml_core)

# GPT-2 inference example
add_executable(gpt2_inference gpt2_inference.c)
target_link_libraries(gpt2_inference ggml_core)

# Benchmark example
add_executable(benchmark benchmark.c)
target_link_libraries(benchmark ggml_core)

# Install examples
install(TARGETS simple_ops gpt2_inference benchmark
    RUNTIME DESTINATION bin/examples)
