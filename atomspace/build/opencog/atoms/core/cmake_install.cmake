# Install script for directory: /workspaces/opencog-central/atomspace/opencog/atoms/core

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so"
         RPATH "/usr/local/lib/opencog")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/atoms/core/libatomcore.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatomcore.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/atoms/core" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/AbsentLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/CondLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/Context.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/DefineLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/DeleteLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/DontExecLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/FindUtils.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/FreeLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/FreeVariables.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/FunctionLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/GrantLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/LambdaLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/NumberNode.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/PrenexLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/PresentLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/PutLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/Quotation.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/RandomChoice.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/Replacement.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/RewriteLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/ScopeLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/SleepLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/StateLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TimeLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypeChoice.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypedAtomLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypedVariableLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypeIntersectionLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypeNode.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/TypeUtils.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/UniqueLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/UnorderedLink.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/Variables.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/VariableList.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/core/VariableSet.h"
    )
endif()

