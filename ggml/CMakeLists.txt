cmake_minimum_required(VERSION 3.12)
project(GGML_OpenCog VERSION 1.0.0 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Find required packages
find_package(PkgConfig REQUIRED)

# Add subdirectories for different components
add_subdirectory(src)
# SkinTwin-ASI Integration
add_library(ggml_skintwin src/ggml_skintwin.c)
target_link_libraries(ggml_skintwin ggml)
target_include_directories(ggml_skintwin PUBLIC include)

# Examples
add_subdirectory(examples)
add_subdirectory(tests)

# Create main GGML library
file(GLOB_RECURSE GGML_SOURCES "src/*.c" "src/*.cpp")
file(GLOB_RECURSE GGML_HEADERS "include/*.h" "include/*.hpp")

add_library(ggml ${GGML_SOURCES})
target_include_directories(ggml PUBLIC include)

# Compiler flags for optimization
if(CMAKE_BUILD_TYPE STREQUAL "Release")
    target_compile_options(ggml PRIVATE -O3 -march=native)
endif()

# Install targets
install(TARGETS ggml
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin)

install(FILES ${GGML_HEADERS} DESTINATION include/ggml)