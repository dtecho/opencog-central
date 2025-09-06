
# Tool executables
add_executable(rwkv_convert rwkv_convert.cpp)
target_link_libraries(rwkv_convert rwkv_cpp_static)

add_executable(rwkv_quantize rwkv_quantize.cpp)
target_link_libraries(rwkv_quantize rwkv_cpp_static)

# Install tools
install(TARGETS rwkv_convert rwkv_quantize
    RUNTIME DESTINATION bin/tools
)
