
# Source files
set(OPENCOG_LLAMA_SOURCES
    opencog_llama.cpp
    atomspace_llama.cpp
    cognitive_inference.cpp
    pattern_matching.cpp
    memory_management.cpp
)

# Create the library
add_library(opencog-llama-core STATIC ${OPENCOG_LLAMA_SOURCES})

target_include_directories(opencog-llama-core PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/../include
    ${CMAKE_CURRENT_SOURCE_DIR}/../../3p/llama.cpp/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../../3p/ggml/include
)

target_compile_features(opencog-llama-core PUBLIC cxx_std_17)
