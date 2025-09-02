# GGML Examples

# Simple tensor operations example
add_executable(simple_ops simple_ops.c)
target_link_libraries(simple_ops ggml_core)

# GPT-2 inference example
add_executable(gpt2_inference gpt2_inference.c)
target_link_libraries(gpt2_inference ggml)

# Benchmark example
add_executable(benchmark benchmark.c)
target_link_libraries(benchmark ggml_core)

# SkinTwin-ASI Examples
add_executable(skintwin_demo skintwin_demo.c)
target_link_libraries(skintwin_demo ggml_skintwin ggml)

add_executable(skintwin_benchmark skintwin_benchmark.c)
target_link_libraries(skintwin_benchmark ggml_skintwin ggml)

add_executable(skintwin_integration skintwin_integration.c)
target_link_libraries(skintwin_integration ggml_skintwin ggml)

# Install examples
install(TARGETS simple_ops gpt2_inference benchmark skintwin_demo skintwin_benchmark skintwin_integration
    RUNTIME DESTINATION bin/examples)