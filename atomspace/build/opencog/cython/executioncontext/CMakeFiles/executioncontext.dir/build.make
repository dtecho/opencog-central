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

# Include any dependencies generated for this target.
include opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/compiler_depend.make

# Include the progress variables for this target.
include opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/progress.make

# Include the compile flags for this target's objects.
include opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/flags.make

opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o: opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/flags.make
opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o: /workspaces/opencog-central/atomspace/opencog/cython/executioncontext/Context.cc
opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o: opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o -MF CMakeFiles/executioncontext.dir/Context.cc.o.d -o CMakeFiles/executioncontext.dir/Context.cc.o -c /workspaces/opencog-central/atomspace/opencog/cython/executioncontext/Context.cc

opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/executioncontext.dir/Context.cc.i"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/opencog/cython/executioncontext/Context.cc > CMakeFiles/executioncontext.dir/Context.cc.i

opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/executioncontext.dir/Context.cc.s"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/opencog/cython/executioncontext/Context.cc -o CMakeFiles/executioncontext.dir/Context.cc.s

# Object files for target executioncontext
executioncontext_OBJECTS = \
"CMakeFiles/executioncontext.dir/Context.cc.o"

# External object files for target executioncontext
executioncontext_EXTERNAL_OBJECTS =

opencog/cython/executioncontext/libexecutioncontext.so: opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/Context.cc.o
opencog/cython/executioncontext/libexecutioncontext.so: opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/build.make
opencog/cython/executioncontext/libexecutioncontext.so: opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libexecutioncontext.so"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/executioncontext.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/build: opencog/cython/executioncontext/libexecutioncontext.so
.PHONY : opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/build

opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext && $(CMAKE_COMMAND) -P CMakeFiles/executioncontext.dir/cmake_clean.cmake
.PHONY : opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/clean

opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/depend:
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/opencog/cython/executioncontext /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext /workspaces/opencog-central/atomspace/build/opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : opencog/cython/executioncontext/CMakeFiles/executioncontext.dir/depend

