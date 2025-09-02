# CMake generated Testfile for 
# Source directory: /home/runner/workspace/ggml/tests
# Build directory: /home/runner/workspace/ggml/build/tests
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(tensor_ops "/home/runner/workspace/ggml/build/tests/test_tensor_ops")
set_tests_properties(tensor_ops PROPERTIES  _BACKTRACE_TRIPLES "/home/runner/workspace/ggml/tests/CMakeLists.txt;9;add_test;/home/runner/workspace/ggml/tests/CMakeLists.txt;0;")
add_test(quantization "/home/runner/workspace/ggml/build/tests/test_quantization")
set_tests_properties(quantization PROPERTIES  _BACKTRACE_TRIPLES "/home/runner/workspace/ggml/tests/CMakeLists.txt;14;add_test;/home/runner/workspace/ggml/tests/CMakeLists.txt;0;")
add_test(backends "/home/runner/workspace/ggml/build/tests/test_backends")
set_tests_properties(backends PROPERTIES  _BACKTRACE_TRIPLES "/home/runner/workspace/ggml/tests/CMakeLists.txt;19;add_test;/home/runner/workspace/ggml/tests/CMakeLists.txt;0;")
