
# Example executables
add_executable(simple_chat simple_chat.cpp)
target_link_libraries(simple_chat rwkv_cpp_static)

add_executable(model_info model_info.cpp)
target_link_libraries(model_info rwkv_cpp_static)

add_executable(benchmark benchmark.cpp)
target_link_libraries(benchmark rwkv_cpp_static)

# Install examples
install(TARGETS simple_chat model_info benchmark
    RUNTIME DESTINATION bin/examples
)
