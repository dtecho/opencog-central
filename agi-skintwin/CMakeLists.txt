
CMAKE_MINIMUM_REQUIRED(VERSION 3.16)
PROJECT(SkinTwin-ASI)

# Set version
SET(SEMANTIC_VERSION 0.1.0)

# Add OpenCog cmake modules to search path
list(APPEND CMAKE_MODULE_PATH
    "${CMAKE_SOURCE_DIR}/cmake"
    "${PROJECT_SOURCE_DIR}/../atomspace/cmake"
    "${PROJECT_SOURCE_DIR}/../cogutil/cmake"
)

# Find required OpenCog components
FIND_PACKAGE(CogUtil 2.0.3 CONFIG REQUIRED)
FIND_PACKAGE(AtomSpace 5.0.4 CONFIG REQUIRED)

# Python bindings
FIND_PACKAGE(PkgConfig REQUIRED)
FIND_PACKAGE(Python3 REQUIRED COMPONENTS Interpreter Development)

# Set C++ standard
SET(CMAKE_CXX_STANDARD 17)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)

# Include directories
INCLUDE_DIRECTORIES(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${COGUTIL_INCLUDE_DIR}
    ${ATOMSPACE_INCLUDE_DIR}
    ${Python3_INCLUDE_DIRS}
)

# Add subdirectories
ADD_SUBDIRECTORY(skin_twin)

# Python module installation
IF(HAVE_CYTHON)
    ADD_SUBDIRECTORY(skin_twin/cython)
ENDIF(HAVE_CYTHON)

# Configuration
CONFIGURE_FILE(${CMAKE_SOURCE_DIR}/lib/SkinTwinConfig.cmake.in
    ${CMAKE_BINARY_DIR}/SkinTwinConfig.cmake @ONLY)

# Installation
INSTALL(FILES
    ${CMAKE_BINARY_DIR}/SkinTwinConfig.cmake
    DESTINATION lib/cmake/SkinTwin)

# Package information
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "SkinTwin-ASI: OpenCog-based Multiscale Skin Modeling System")
SET(CPACK_PACKAGE_NAME "SkinTwin-ASI")
SET(CPACK_PACKAGE_VENDOR "SkinTwin Development Team")
SET(CPACK_PACKAGE_VERSION ${SEMANTIC_VERSION})

INCLUDE(CPack)
