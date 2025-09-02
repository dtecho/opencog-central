
cmake_minimum_required(VERSION 3.12)
project(rwkv-cpp-implementation VERSION 1.0.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find packages
find_package(Threads REQUIRED)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../3p/rwkv.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/../3p/ggml/include)

# Add subdirectories
add_subdirectory(src)
add_subdirectory(examples)
add_subdirectory(tools)

# Optional Python bindings
option(BUILD_PYTHON_BINDINGS "Build Python bindings" OFF)
if(BUILD_PYTHON_BINDINGS)
    add_subdirectory(bindings/python)
endif()

# Optional tests
option(BUILD_TESTS "Build tests" OFF)
if(BUILD_TESTS)
    enable_testing()
    add_subdirectory(tests)
endif()

# Optional: Add tests if needed
if(BUILD_TESTING)
    add_subdirectory(tests)
endif()

# Set default build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# Compiler flags
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -DNDEBUG")
set(CMAKE_CXX_FLAGS_DEBUG "-g -O0")
