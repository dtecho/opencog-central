# Install script for directory: /workspaces/opencog-central/atomspace/opencog/atoms/foreign

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so"
         RPATH "/usr/local/lib/opencog")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign/libforeign.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libforeign.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/atoms/foreign" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/opencog/atoms/foreign/DatalogAST.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/foreign/ForeignAST.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/foreign/SexprAST.h"
    )
endif()

