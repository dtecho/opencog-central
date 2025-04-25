# Install script for directory: /workspaces/opencog-central/atomspace/tests/atoms

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

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/atom_types/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/base/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/core/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/execution/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/rule/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/join/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/parallel/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/truthvalue/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/value/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/reduct/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/flow/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/pattern/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/tests/atoms/foreign/cmake_install.cmake")

endif()

