# Install script for directory: /workspaces/opencog-central/atomspace/cmake

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/opencog/cmake/OpenCogAtomTypes.cmake;/usr/local/share/opencog/cmake/OpenCogCython.cmake;/usr/local/share/opencog/cmake/OpenCogGenCxxTypes.cmake;/usr/local/share/opencog/cmake/OpenCogGenOCamlTypes.cmake;/usr/local/share/opencog/cmake/OpenCogGenPythonTypes.cmake;/usr/local/share/opencog/cmake/OpenCogGenScmTypes.cmake;/usr/local/share/opencog/cmake/OpenCogGenTypes.cmake;/usr/local/share/opencog/cmake/OpenCogGenWrapper.cmake;/usr/local/share/opencog/cmake/OpenCogGuile.cmake;/usr/local/share/opencog/cmake/OpenCogOCaml.cmake;/usr/local/share/opencog/cmake/OpenCogMacros.cmake;/usr/local/share/opencog/cmake/OpenCogFunctions.cmake")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/opencog/cmake" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/cmake/OpenCogAtomTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogCython.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenCxxTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenOCamlTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenPythonTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenScmTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenTypes.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGenWrapper.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogOCaml.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogMacros.cmake"
    "/workspaces/opencog-central/atomspace/cmake/OpenCogFunctions.cmake"
    )
endif()

