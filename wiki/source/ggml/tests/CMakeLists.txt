
# GGML Tests

enable_testing()

# Test tensor operations
add_executable(test_tensor_ops test_tensor_ops.c)
target_link_libraries(test_tensor_ops ggml_core)
add_test(NAME tensor_ops COMMAND test_tensor_ops)

# Test quantization
add_executable(test_quantization test_quantization.c)
target_link_libraries(test_quantization ggml_core)
add_test(NAME quantization COMMAND test_quantization)

# Test backend compatibility
add_executable(test_backends test_backends.c)
target_link_libraries(test_backends ggml_core)
add_test(NAME backends COMMAND test_backends)
