# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /workspaces/opencog-central/atomspace

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /workspaces/opencog-central/atomspace/build

# Utility rule file for COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.

# Include any custom commands dependencies for this target.
include opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/compiler_depend.make

# Include the progress variables for this target.
include opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/progress.make

COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython: opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/build.make
	cd /workspaces/opencog-central/atomspace/build/opencog/cython && /usr/bin/cmake -E copy /workspaces/opencog-central/atomspace/opencog/cython/opencog//python.scm /workspaces/opencog-central/atomspace/build/opencog/scm//opencog/python.scm
	cd /workspaces/opencog-central/atomspace/build/opencog/cython && /usr/bin/cmake -E copy /workspaces/opencog-central/atomspace/opencog/cython/opencog//python.scm /workspaces/opencog-central/atomspace/build/opencog/scm//opencog/python.scm
.PHONY : COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython

# Rule to build all files generated by this target.
opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/build: COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython
.PHONY : opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/build

opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/opencog/cython && $(CMAKE_COMMAND) -P CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/cmake_clean.cmake
.PHONY : opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/clean

opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/depend:
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/opencog/cython /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/opencog/cython /workspaces/opencog-central/atomspace/build/opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : opencog/cython/CMakeFiles/COPY_TO_LOAD_PATH_IN_BUILD_DIR_FROM__workspaces_opencog-central_atomspace_opencog_cython.dir/depend

