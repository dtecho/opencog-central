
cmake_minimum_required(VERSION 3.18)
project(llama-cpp-opencog)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(PkgConfig REQUIRED)

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../3p/ggml/include
)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(tools)

# Build shared library
add_library(llama-cpp-opencog SHARED
    src/opencog_llama.cpp
    src/atomspace_llama.cpp
    src/cognitive_inference.cpp
    src/pattern_matching.cpp
    src/memory_management.cpp
)

target_link_libraries(llama-cpp-opencog
    ${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/build/libllama.so
    ${CMAKE_CURRENT_SOURCE_DIR}/../ggml/build/libggml.a
)

# Install targets
install(TARGETS llama-cpp-opencog
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)

install(DIRECTORY include/
    DESTINATION include/llama-cpp-opencog
)
