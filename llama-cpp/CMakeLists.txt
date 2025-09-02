
cmake_minimum_required(VERSION 3.12)
project(OpenCogLlama VERSION 1.0.0 LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add compiler flags for optimization and debugging
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -O3")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0 -DDEBUG")

# Find required packages
find_package(PkgConfig REQUIRED)

# Try to find OpenCog components
find_package(CogUtil QUIET)
find_package(AtomSpace QUIET)

# If OpenCog is not found, provide fallback includes
if(NOT CogUtil_FOUND OR NOT AtomSpace_FOUND)
    message(WARNING "OpenCog libraries not found. Using fallback implementations.")
    add_definitions(-DUSE_FALLBACK_OPENCOG)
endif()

# Find Threads (required for llama.cpp)
find_package(Threads REQUIRED)

# Find OpenMP if available
find_package(OpenMP)
if(OpenMP_CXX_FOUND)
    target_link_libraries(opencog_llama PUBLIC OpenMP::OpenMP_CXX)
endif()

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/include
    ${CMAKE_CURRENT_SOURCE_DIR}/../3p/ggml/include
)

# Conditional OpenCog includes
if(CogUtil_FOUND AND AtomSpace_FOUND)
    include_directories(
        ${COGUTIL_INCLUDE_DIR}
        ${ATOMSPACE_INCLUDE_DIR}
    )
endif()

# Source files
set(OPENCOG_LLAMA_SOURCES
    src/opencog_llama.cpp
)

# Create the main library
add_library(opencog_llama SHARED ${OPENCOG_LLAMA_SOURCES})

# Link libraries
target_link_libraries(opencog_llama
    Threads::Threads
)

# Conditional OpenCog linking
if(CogUtil_FOUND AND AtomSpace_FOUND)
    target_link_libraries(opencog_llama
        ${COGUTIL_LIBRARIES}
        ${ATOMSPACE_LIBRARIES}
    )
endif()

# Link with llama.cpp if available
if(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/libllama.so")
    target_link_libraries(opencog_llama
        "${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/libllama.so"
    )
elseif(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/libllama.a")
    target_link_libraries(opencog_llama
        "${CMAKE_CURRENT_SOURCE_DIR}/../3p/llama.cpp/libllama.a"
    )
endif()

# Set target properties
set_target_properties(opencog_llama PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION 1
    PUBLIC_HEADER "include/opencog_llama.h;include/atomspace_llama.h"
)

# Examples
add_executable(basic_reasoning examples/basic_reasoning.cpp)
target_link_libraries(basic_reasoning opencog_llama)

# Tools
add_executable(cognitive_shell tools/cognitive_shell.cpp)
target_link_libraries(cognitive_shell opencog_llama)

# Install targets
install(TARGETS opencog_llama
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include/opencog_llama
)

install(TARGETS basic_reasoning cognitive_shell
    RUNTIME DESTINATION bin
)

# Install documentation
install(FILES README.md
    DESTINATION share/doc/opencog_llama
)

# CPack configuration for packaging
set(CPACK_PACKAGE_NAME "opencog-llama")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "OpenCog integration with llama.cpp for cognitive AI")
set(CPACK_PACKAGE_CONTACT "opencog-dev@opencog.org")

include(CPack)

# Add tests if testing is enabled
option(ENABLE_TESTS "Enable testing" ON)
if(ENABLE_TESTS)
    enable_testing()
    
    # Basic functionality test
    add_test(NAME basic_reasoning_test
        COMMAND basic_reasoning
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
    
    # Shell command test
    add_test(NAME cognitive_shell_test
        COMMAND cognitive_shell --help
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endif()

# Documentation generation with Doxygen
find_package(Doxygen QUIET)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/../docs/Doxyfile.in
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(doc
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM
    )
endif()

# Debug information
message(STATUS "OpenCog-Llama Configuration:")
message(STATUS "  Version: ${PROJECT_VERSION}")
message(STATUS "  CXX Standard: ${CMAKE_CXX_STANDARD}")
message(STATUS "  Build Type: ${CMAKE_BUILD_TYPE}")
message(STATUS "  CogUtil Found: ${CogUtil_FOUND}")
message(STATUS "  AtomSpace Found: ${AtomSpace_FOUND}")
message(STATUS "  OpenMP Found: ${OpenMP_CXX_FOUND}")
message(STATUS "  Doxygen Found: ${DOXYGEN_FOUND}")
message(STATUS "  Install Prefix: ${CMAKE_INSTALL_PREFIX}")
