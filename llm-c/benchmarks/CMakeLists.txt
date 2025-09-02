
# Benchmarks
add_executable(performance_test performance_test.c)
target_link_libraries(performance_test llm_core m)

# Copy to build directory
add_custom_target(benchmarks ALL DEPENDS performance_test)
