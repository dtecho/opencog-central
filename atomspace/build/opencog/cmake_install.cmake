# Install script for directory: /workspaces/opencog-central/atomspace/opencog

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
   "/usr/local/share/guile/site/3.0/opencog/as-config.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog" TYPE FILE MESSAGE_LAZY RENAME "as-config.scm" FILES "/workspaces/opencog-central/atomspace/build/opencog/scm/opencog/as-config-installable.scm")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/workspaces/opencog-central/atomspace/build/opencog/atoms/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/atomspace/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/eval/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/query/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/persist/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/guile/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/scm/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/matrix/cmake_install.cmake")
  include("/workspaces/opencog-central/atomspace/build/opencog/cython/cmake_install.cmake")

endif()

