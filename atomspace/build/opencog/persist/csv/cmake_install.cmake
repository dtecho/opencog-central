# Install script for directory: /workspaces/opencog-central/atomspace/opencog/persist/csv

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
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so"
         RPATH "/usr/local/lib/opencog")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/persist/csv/libcsv.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/persist/csv" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/persist/csv/table_read.h")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/persist/csv/libcsv-table.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/persist/csv:/workspaces/opencog-central/atomspace/build/opencog/guile:/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign:/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/opencog/libcsv-table.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  
              IF(EXISTS
                     /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm
                 AND NOT
                     /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm
                   STREQUAL
                     /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm
                 AND
                     /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm
                   IS_NEWER_THAN
                     /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm
                 )
                 MESSAGE("-- Touch: /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm")
                 MESSAGE("-- Newer: /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm")
                 FILE(TOUCH /workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm)
              ENDIF()
            
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/share/guile/site/3.0/opencog/csv-table.scm")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/share/guile/site/3.0/opencog" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/persist/csv/opencog/csv-table.scm")
endif()

