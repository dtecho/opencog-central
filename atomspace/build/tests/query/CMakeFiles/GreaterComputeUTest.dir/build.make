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
include tests/query/CMakeFiles/GreaterComputeUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/query/CMakeFiles/GreaterComputeUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/query/CMakeFiles/GreaterComputeUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/query/CMakeFiles/GreaterComputeUTest.dir/flags.make

tests/query/GreaterComputeUTest.cpp: /workspaces/opencog-central/atomspace/tests/query/GreaterComputeUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating GreaterComputeUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/query/GreaterComputeUTest.cpp /workspaces/opencog-central/atomspace/tests/query/GreaterComputeUTest.cxxtest

tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o: tests/query/CMakeFiles/GreaterComputeUTest.dir/flags.make
tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o: tests/query/GreaterComputeUTest.cpp
tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o: tests/query/CMakeFiles/GreaterComputeUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o -MF CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o.d -o CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/query/GreaterComputeUTest.cpp

tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/query/GreaterComputeUTest.cpp > CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.i

tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/query/GreaterComputeUTest.cpp -o CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.s

# Object files for target GreaterComputeUTest
GreaterComputeUTest_OBJECTS = \
"CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o"

# External object files for target GreaterComputeUTest
GreaterComputeUTest_EXTERNAL_OBJECTS =

tests/query/GreaterComputeUTest: tests/query/CMakeFiles/GreaterComputeUTest.dir/GreaterComputeUTest.cpp.o
tests/query/GreaterComputeUTest: tests/query/CMakeFiles/GreaterComputeUTest.dir/build.make
tests/query/GreaterComputeUTest: opencog/guile/modules/liblogger.so
tests/query/GreaterComputeUTest: opencog/guile/libsmob.so
tests/query/GreaterComputeUTest: opencog/atoms/foreign/libforeign.so
tests/query/GreaterComputeUTest: opencog/persist/prolog/libdatalog.so
tests/query/GreaterComputeUTest: opencog/atomspace/libatomspace.so
tests/query/GreaterComputeUTest: opencog/atoms/pattern/libpattern.so
tests/query/GreaterComputeUTest: opencog/query/libquery-engine.so
tests/query/GreaterComputeUTest: opencog/atoms/rule/librule.so
tests/query/GreaterComputeUTest: opencog/atoms/execution/libexecution.so
tests/query/GreaterComputeUTest: opencog/atoms/reduct/libclearbox.so
tests/query/GreaterComputeUTest: opencog/atoms/parallel/libparallel.so
tests/query/GreaterComputeUTest: opencog/atoms/flow/libatomflow.so
tests/query/GreaterComputeUTest: opencog/atoms/join/libjoin.so
tests/query/GreaterComputeUTest: opencog/atoms/core/libatomcore.so
tests/query/GreaterComputeUTest: opencog/atoms/grounded/libgrounded.so
tests/query/GreaterComputeUTest: opencog/atoms/base/libatombase.so
tests/query/GreaterComputeUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/query/GreaterComputeUTest: opencog/atoms/value/libvalue.so
tests/query/GreaterComputeUTest: opencog/atoms/atom_types/libatom_types.so
tests/query/GreaterComputeUTest: /usr/local/lib/libguile-3.0.so
tests/query/GreaterComputeUTest: /usr/local/lib/opencog/libcogutil.so
tests/query/GreaterComputeUTest: tests/query/CMakeFiles/GreaterComputeUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable GreaterComputeUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/GreaterComputeUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/query/CMakeFiles/GreaterComputeUTest.dir/build: tests/query/GreaterComputeUTest
.PHONY : tests/query/CMakeFiles/GreaterComputeUTest.dir/build

tests/query/CMakeFiles/GreaterComputeUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -P CMakeFiles/GreaterComputeUTest.dir/cmake_clean.cmake
.PHONY : tests/query/CMakeFiles/GreaterComputeUTest.dir/clean

tests/query/CMakeFiles/GreaterComputeUTest.dir/depend: tests/query/GreaterComputeUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/query /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/query /workspaces/opencog-central/atomspace/build/tests/query/CMakeFiles/GreaterComputeUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/query/CMakeFiles/GreaterComputeUTest.dir/depend

