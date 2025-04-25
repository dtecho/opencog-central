# Install script for directory: /workspaces/opencog-central/atomspace/opencog/scm

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
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/apply.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/apply.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/apply.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-cache.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-cache.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-cache.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-docs.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-docs.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-docs.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/core-docs.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/core-docs.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/core-docs.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/debug-trace.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/debug-trace.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/debug-trace.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/file-utils.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/file-utils.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/file-utils.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/repl-shell.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/repl-shell.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/repl-shell.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/tv.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/tv.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/tv.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/types.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/types.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/types.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/utilities.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/utilities.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/base/utilities.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/apply.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/apply.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/atom-cache.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-cache.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/atom-docs.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/atom-docs.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/core-docs.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/core-docs.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/debug-trace.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/debug-trace.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/file-utils.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/file-utils.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/repl-shell.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/repl-shell.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/tv.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/tv.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/types.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/types.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/base/utilities.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog/base" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/base/utilities.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/extension.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/extension.scm")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/test-runner.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/scm/opencog/test-runner.scm")
endif()

