cmake_minimum_required(VERSION 3.12)
project(llm-c VERSION 1.0.0 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Find required packages
find_package(PkgConfig REQUIRED)

# Include directories
include_directories(include)
include_directories(${CMAKE_SOURCE_DIR}/3p/llm.c/include)

# Add source files
set(SOURCES
    src/transformer.c
    src/sampling.c
    src/tokenizer.c
    src/generation.c
    src/memory_management.c
    src/attention.c
    src/activations.c
    src/optimization.c
    src/model_loader.c
    src/quantization.c
    src/atomspace_bridge.c
    src/cognitive_reasoning.c
    src/ecan_attention.c
    src/scheme_interface.c
    src/moses_evolution.c
    src/pattern_mining.c
)

# Create library
add_library(llm-c ${SOURCES})

# Link against system libraries
target_link_libraries(llm-c m)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(tests)
add_subdirectory(benchmarks)

# Install targets
install(TARGETS llm-c DESTINATION lib)
install(DIRECTORY include/ DESTINATION include)

# Build model converter tool
add_executable(model_converter tools/model_converter.c)
target_link_libraries(model_converter llm_core)

# Build OpenCog integration tools
add_executable(atomese_converter tools/atomese_converter.c)
target_link_libraries(atomese_converter llm_core)

add_executable(opencog_integration examples/opencog_integration.c)
target_link_libraries(opencog_integration llm_core)