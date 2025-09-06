
# Tests
add_executable(test_transformer tests/test_transformer.c)
target_link_libraries(test_transformer llm-c)

add_executable(test_tokenizer tests/test_tokenizer.c)
target_link_libraries(test_tokenizer llm-c)

add_test(NAME test_transformer COMMAND test_transformer)
add_test(NAME test_tokenizer COMMAND test_tokenizer)
