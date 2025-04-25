# Install script for directory: /workspaces/opencog-central/atomspace/opencog/cython/opencog

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opencog/cython/opencog" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/__init__.py"
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/atomspace.pxd"
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/logger.pxd"
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/value_types.pxd"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/atomspace.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/guile:/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign:/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/atomspace.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/execute.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/execute.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog:/workspaces/opencog-central/atomspace/build/opencog/guile:/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign:/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/execute.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/logger.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/logger.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so"
         OLD_RPATH "/usr/local/lib/opencog::::::::::::::::::::::::::::::::::::::::::::::::"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/logger.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/type_constructors.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/type_constructors.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/utilities.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/utilities.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/cython:/workspaces/opencog-central/atomspace/build/opencog/cython/opencog:/workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext:/workspaces/opencog-central/atomspace/build/opencog/persist/file:/workspaces/opencog-central/atomspace/build/opencog/persist/sexcom:/workspaces/opencog-central/atomspace/build/opencog/persist/proxy:/workspaces/opencog-central/atomspace/build/opencog/persist/api:/workspaces/opencog-central/atomspace/build/opencog/persist/storage:/workspaces/opencog-central/atomspace/build/opencog/guile:/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign:/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/usr/local/lib:/workspaces/opencog-central/atomspace/build/opencog/persist/sexpr:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/utilities.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/bindlink.py;/usr/local/lib/python3.11/dist-packages/opencog/exec.py;/usr/local/lib/python3.11/dist-packages/opencog/scheme_wrapper.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE FILE MESSAGE_LAZY FILES
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/bindlink.py"
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/exec.py"
    "/workspaces/opencog-central/atomspace/opencog/cython/opencog/scheme_wrapper.py"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so"
         RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
  endif()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/scheme.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE SHARED_LIBRARY MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog/scheme.so")
  if(EXISTS "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so"
         OLD_RPATH "/workspaces/opencog-central/atomspace/build/opencog/cython/opencog:/workspaces/opencog-central/atomspace/build/opencog/guile:/workspaces/opencog-central/atomspace/build/opencog/atoms/foreign:/workspaces/opencog-central/atomspace/build/opencog/persist/prolog:/workspaces/opencog-central/atomspace/build/opencog/atomspace:/workspaces/opencog-central/atomspace/build/opencog/atoms/join:/workspaces/opencog-central/atomspace/build/opencog/atoms/pattern:/workspaces/opencog-central/atomspace/build/opencog/query:/workspaces/opencog-central/atomspace/build/opencog/atoms/rule:/workspaces/opencog-central/atomspace/build/opencog/atoms/grounded:/workspaces/opencog-central/atomspace/build/opencog/atoms/execution:/workspaces/opencog-central/atomspace/build/opencog/atoms/reduct:/workspaces/opencog-central/atomspace/build/opencog/atoms/flow:/workspaces/opencog-central/atomspace/build/opencog/atoms/parallel:/workspaces/opencog-central/atomspace/build/opencog/atoms/core:/workspaces/opencog-central/atomspace/build/opencog/atoms/base:/workspaces/opencog-central/atomspace/build/opencog/atoms/truthvalue:/workspaces/opencog-central/atomspace/build/opencog/atoms/value:/workspaces/opencog-central/atomspace/build/opencog/atoms/atom_types:/usr/local/lib:/usr/local/lib/opencog:"
         NEW_RPATH "/usr/local/lib/opencog:/usr/local/lib/python3.11/dist-packages/opencog:/usr/local/lib")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}/usr/local/lib/python3.11/dist-packages/opencog/scheme.so")
    endif()
  endif()
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/python3.11/dist-packages/opencog/__init__.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  file(INSTALL DESTINATION "/usr/local/lib/python3.11/dist-packages/opencog" TYPE FILE MESSAGE_LAZY FILES "/workspaces/opencog-central/atomspace/opencog/cython/opencog/__init__.py")
endif()

