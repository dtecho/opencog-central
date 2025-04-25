# Install script for directory: /workspaces/opencog-central/atomspace/opencog/atoms/atom_types

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so"
         RPATH "/usr/local/lib/opencog")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/libatom_types.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so"
         OLD_RPATH "/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libatom_types.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/atoms/atom_types" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/atom_types.h"
    "/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/atom_names.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/atom_types/atom_types.cc"
    "/workspaces/opencog-central/atomspace/opencog/atoms/atom_types/NameServer.h"
    "/workspaces/opencog-central/atomspace/opencog/atoms/atom_types/types.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/atoms/atom_types//workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/core_types.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types/core_types.scm")
endif()

