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
include tests/atomspace/CMakeFiles/UseCountUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atomspace/CMakeFiles/UseCountUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atomspace/CMakeFiles/UseCountUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atomspace/CMakeFiles/UseCountUTest.dir/flags.make

tests/atomspace/UseCountUTest.cpp: /workspaces/opencog-central/atomspace/tests/atomspace/UseCountUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating UseCountUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atomspace/UseCountUTest.cpp /workspaces/opencog-central/atomspace/tests/atomspace/UseCountUTest.cxxtest

tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o: tests/atomspace/CMakeFiles/UseCountUTest.dir/flags.make
tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o: tests/atomspace/UseCountUTest.cpp
tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o: tests/atomspace/CMakeFiles/UseCountUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o -MF CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o.d -o CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atomspace/UseCountUTest.cpp

tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atomspace/UseCountUTest.cpp > CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.i

tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atomspace/UseCountUTest.cpp -o CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.s

# Object files for target UseCountUTest
UseCountUTest_OBJECTS = \
"CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o"

# External object files for target UseCountUTest
UseCountUTest_EXTERNAL_OBJECTS =

tests/atomspace/UseCountUTest: tests/atomspace/CMakeFiles/UseCountUTest.dir/UseCountUTest.cpp.o
tests/atomspace/UseCountUTest: tests/atomspace/CMakeFiles/UseCountUTest.dir/build.make
tests/atomspace/UseCountUTest: opencog/guile/libsmob.so
tests/atomspace/UseCountUTest: opencog/atoms/foreign/libforeign.so
tests/atomspace/UseCountUTest: opencog/persist/prolog/libdatalog.so
tests/atomspace/UseCountUTest: opencog/atomspace/libatomspace.so
tests/atomspace/UseCountUTest: opencog/atoms/join/libjoin.so
tests/atomspace/UseCountUTest: opencog/atoms/pattern/libpattern.so
tests/atomspace/UseCountUTest: opencog/query/libquery-engine.so
tests/atomspace/UseCountUTest: opencog/atoms/rule/librule.so
tests/atomspace/UseCountUTest: opencog/atoms/grounded/libgrounded.so
tests/atomspace/UseCountUTest: opencog/atoms/execution/libexecution.so
tests/atomspace/UseCountUTest: opencog/atoms/reduct/libclearbox.so
tests/atomspace/UseCountUTest: opencog/atoms/flow/libatomflow.so
tests/atomspace/UseCountUTest: opencog/atoms/parallel/libparallel.so
tests/atomspace/UseCountUTest: opencog/atoms/core/libatomcore.so
tests/atomspace/UseCountUTest: opencog/atoms/base/libatombase.so
tests/atomspace/UseCountUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atomspace/UseCountUTest: opencog/atoms/value/libvalue.so
tests/atomspace/UseCountUTest: opencog/atoms/atom_types/libatom_types.so
tests/atomspace/UseCountUTest: /usr/local/lib/libguile-3.0.so
tests/atomspace/UseCountUTest: /usr/local/lib/opencog/libcogutil.so
tests/atomspace/UseCountUTest: tests/atomspace/CMakeFiles/UseCountUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable UseCountUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/UseCountUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atomspace/CMakeFiles/UseCountUTest.dir/build: tests/atomspace/UseCountUTest
.PHONY : tests/atomspace/CMakeFiles/UseCountUTest.dir/build

tests/atomspace/CMakeFiles/UseCountUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atomspace && $(CMAKE_COMMAND) -P CMakeFiles/UseCountUTest.dir/cmake_clean.cmake
.PHONY : tests/atomspace/CMakeFiles/UseCountUTest.dir/clean

tests/atomspace/CMakeFiles/UseCountUTest.dir/depend: tests/atomspace/UseCountUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atomspace /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atomspace /workspaces/opencog-central/atomspace/build/tests/atomspace/CMakeFiles/UseCountUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atomspace/CMakeFiles/UseCountUTest.dir/depend

