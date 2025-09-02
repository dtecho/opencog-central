cmake_minimum_required(VERSION 3.12)
project(SkinTwin VERSION 1.0.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
find_package(PkgConfig REQUIRED)
find_package(OpenMP REQUIRED)
find_package(Boost REQUIRED COMPONENTS system filesystem thread)

# Find OpenCog components
find_package(CogUtil 2.0.3 REQUIRED)
find_package(AtomSpace 5.0.4 REQUIRED)
find_package(CogServer 1.0.0 REQUIRED)

# Find Python and Cython
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(Cython 0.29 REQUIRED)

# Include directories
include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}/src
    ${CMAKE_CURRENT_SOURCE_DIR}/agi-bio
    ${CMAKE_CURRENT_SOURCE_DIR}/cheminformatics
    ${ATOMSPACE_INCLUDE_DIR}
    ${COGUTIL_INCLUDE_DIR}
    ${Boost_INCLUDE_DIRS}
    ${Python3_INCLUDE_DIRS}
)

# Add subdirectories
add_subdirectory(src)

# Create SkinTwin library
set(SKINTWIN_SOURCES
    src/core/SkinAtomSpace.cpp
    src/core/SkinAtomTypes.cpp
    src/multiscale/MultiscaleModel.cpp
    src/integration/BiologicalIntegration.cpp
    src/integration/ChemicalIntegration.cpp
)

add_library(skintwin SHARED ${SKINTWIN_SOURCES})

target_link_libraries(skintwin
    ${ATOMSPACE_LIBRARIES}
    ${COGUTIL_LIBRARIES}
    ${Boost_LIBRARIES}
    OpenMP::OpenMP_CXX
)

# Set library properties
set_target_properties(skintwin PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION 1
    OUTPUT_NAME "skintwin"
)

# Install library
install(TARGETS skintwin
    EXPORT SkinTwinTargets
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
    RUNTIME DESTINATION bin
)

# Install headers
install(DIRECTORY src/
    DESTINATION include/skintwin
    FILES_MATCHING PATTERN "*.h"
)

# Create package config files
include(CMakePackageConfigHelpers)

configure_package_config_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/SkinTwinConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfig.cmake
    INSTALL_DESTINATION lib/cmake/SkinTwin
)

write_basic_package_version_file(
    ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfigVersion.cmake
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

export(EXPORT SkinTwinTargets
    FILE ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinTargets.cmake
)

install(EXPORT SkinTwinTargets
    FILE SkinTwinTargets.cmake
    DESTINATION lib/cmake/SkinTwin
)

install(FILES
    ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfig.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfigVersion.cmake
    DESTINATION lib/cmake/SkinTwin
)

# Build Cython extensions
add_custom_target(cython_extensions ALL
    COMMAND ${Python3_EXECUTABLE} setup.py build_ext --inplace
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    COMMENT "Building Cython extensions"
)

add_dependencies(cython_extensions skintwin)

# Enable testing
enable_testing()
add_subdirectory(tests)

# Documentation
find_package(Doxygen)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in
                   ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(doc
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen" VERBATIM
    )
endif()

# Package information
set(CPACK_PACKAGE_NAME "SkinTwin")
set(CPACK_PACKAGE_VERSION ${PROJECT_VERSION})
set(CPACK_PACKAGE_DESCRIPTION "Multiscale Computational Skin Model for OpenCog")
set(CPACK_PACKAGE_CONTACT "skintwin@opencog.org")

include(CPack)