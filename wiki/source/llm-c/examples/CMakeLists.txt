
# Examples
add_executable(run examples/run.c)
target_link_libraries(run llm-c)

add_executable(chat examples/chat.c)
target_link_libraries(chat llm-c)

add_executable(benchmark examples/benchmark.c)
target_link_libraries(benchmark llm-c)
