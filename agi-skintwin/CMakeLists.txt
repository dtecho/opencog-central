
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
CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
PROJECT(SkinTwin)

# Set C++ standard
SET(CMAKE_CXX_STANDARD 17)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find required packages
FIND_PACKAGE(OpenCog REQUIRED)
FIND_PACKAGE(PkgConfig REQUIRED)
FIND_PACKAGE(Boost REQUIRED COMPONENTS system filesystem thread)
FIND_PACKAGE(Python3 COMPONENTS Interpreter Development REQUIRED)

# Include directories
INCLUDE_DIRECTORIES(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${OpenCog_INCLUDE_DIRS}
    ${Python3_INCLUDE_DIRS}
    ${CMAKE_CURRENT_SOURCE_DIR}/agi-bio
    ${CMAKE_CURRENT_SOURCE_DIR}/cheminformatics
)

# Set up compilation flags
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -O3")
SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -g -O0")

# Core library
SET(SKIN_CORE_SOURCES
    src/core/SkinAtomSpace.cpp
    src/multiscale/MultiscaleModel.cpp
    src/integration/BiologicalIntegration.cpp
    src/integration/ChemicalIntegration.cpp
)

ADD_LIBRARY(skintwin-core SHARED ${SKIN_CORE_SOURCES})

TARGET_LINK_LIBRARIES(skintwin-core
    ${OpenCog_LIBRARIES}
    ${Boost_LIBRARIES}
    agi-bio
    cheminformatics
)

# Cython bindings
FIND_PACKAGE(Cython REQUIRED)

SET(CYTHON_FLAGS "--cplus")
SET(CYTHON_SOURCES
    src/cython/skin_cython.pyx
)

# Generate C++ from Cython
FOREACH(pyx_file ${CYTHON_SOURCES})
    GET_FILENAME_COMPONENT(module_name ${pyx_file} NAME_WE)
    SET(cpp_file "${CMAKE_CURRENT_BINARY_DIR}/${module_name}.cpp")
    
    ADD_CUSTOM_COMMAND(
        OUTPUT ${cpp_file}
        COMMAND ${CYTHON_EXECUTABLE} ${CYTHON_FLAGS} -o ${cpp_file} ${CMAKE_CURRENT_SOURCE_DIR}/${pyx_file}
        DEPENDS ${pyx_file}
        COMMENT "Generating ${cpp_file} from ${pyx_file}"
    )
    
    PYTHON3_ADD_LIBRARY(${module_name} MODULE ${cpp_file})
    TARGET_LINK_LIBRARIES(${module_name} skintwin-core ${Python3_LIBRARIES})
    
    # Set properties for Python module
    SET_TARGET_PROPERTIES(${module_name} PROPERTIES 
        PREFIX ""
        SUFFIX "${Python3_SOABI}"
    )
    
ENDFOREACH()

# Tests
ENABLE_TESTING()

SET(TEST_SOURCES
    tests/test_skin_atomspace.cpp
    tests/test_multiscale_model.cpp
    tests/test_biological_integration.cpp
    tests/test_chemical_integration.cpp
)

FOREACH(test_file ${TEST_SOURCES})
    GET_FILENAME_COMPONENT(test_name ${test_file} NAME_WE)
    ADD_EXECUTABLE(${test_name} ${test_file})
    TARGET_LINK_LIBRARIES(${test_name} skintwin-core ${OpenCog_LIBRARIES})
    ADD_TEST(NAME ${test_name} COMMAND ${test_name})
ENDFOREACH()

# Installation
INSTALL(TARGETS skintwin-core
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

INSTALL(DIRECTORY src/
    DESTINATION include/skintwin
    FILES_MATCHING PATTERN "*.h"
)

# Python package installation
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/skin_cython.so
    DESTINATION ${Python3_SITEARCH}/skintwin
)

# Configuration file
CONFIGURE_FILE(
    ${CMAKE_CURRENT_SOURCE_DIR}/lib/SkinTwinConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfig.cmake
    @ONLY
)

INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/SkinTwinConfig.cmake
    DESTINATION lib/cmake/SkinTwin
)
