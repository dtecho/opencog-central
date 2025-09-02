cmake_minimum_required(VERSION 3.12)
project(llm-c VERSION 1.0.0 LANGUAGES C CXX)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)

# Find required packages
find_package(PkgConfig REQUIRED)

# Include directories
include_directories(include)
include_directories(${CMAKE_SOURCE_DIR}/3p/llm.c/include)

# Source files
file(GLOB_RECURSE SOURCES "src/*.c" "src/*.cpp")

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