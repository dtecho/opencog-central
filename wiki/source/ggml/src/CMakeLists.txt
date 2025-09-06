
# GGML Core Implementation

file(GLOB GGML_CORE_SOURCES "*.c" "*.cpp")
file(GLOB GGML_CORE_HEADERS "../include/*.h" "../include/*.hpp")

add_library(ggml_core ${GGML_CORE_SOURCES})
target_include_directories(ggml_core PUBLIC ../include)

# Add specific source files for different backends
if(GGML_CUDA)
    file(GLOB CUDA_SOURCES "cuda/*.cu" "cuda/*.cpp")
    add_library(ggml_cuda ${CUDA_SOURCES})
    target_link_libraries(ggml_core ggml_cuda)
endif()

if(GGML_METAL)
    file(GLOB METAL_SOURCES "metal/*.m" "metal/*.mm")
    add_library(ggml_metal ${METAL_SOURCES})
    target_link_libraries(ggml_core ggml_metal)
endif()

# OpenMP support
find_package(OpenMP)
if(OpenMP_C_FOUND)
    target_link_libraries(ggml_core OpenMP::OpenMP_C)
endif()
