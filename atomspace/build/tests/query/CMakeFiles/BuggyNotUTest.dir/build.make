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
include tests/query/CMakeFiles/BuggyNotUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/query/CMakeFiles/BuggyNotUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/query/CMakeFiles/BuggyNotUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/query/CMakeFiles/BuggyNotUTest.dir/flags.make

tests/query/BuggyNotUTest.cpp: /workspaces/opencog-central/atomspace/tests/query/BuggyNotUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating BuggyNotUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/query/BuggyNotUTest.cpp /workspaces/opencog-central/atomspace/tests/query/BuggyNotUTest.cxxtest

tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o: tests/query/CMakeFiles/BuggyNotUTest.dir/flags.make
tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o: tests/query/BuggyNotUTest.cpp
tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o: tests/query/CMakeFiles/BuggyNotUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o -MF CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o.d -o CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/query/BuggyNotUTest.cpp

tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/query/BuggyNotUTest.cpp > CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.i

tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/query/BuggyNotUTest.cpp -o CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.s

# Object files for target BuggyNotUTest
BuggyNotUTest_OBJECTS = \
"CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o"

# External object files for target BuggyNotUTest
BuggyNotUTest_EXTERNAL_OBJECTS =

tests/query/BuggyNotUTest: tests/query/CMakeFiles/BuggyNotUTest.dir/BuggyNotUTest.cpp.o
tests/query/BuggyNotUTest: tests/query/CMakeFiles/BuggyNotUTest.dir/build.make
tests/query/BuggyNotUTest: opencog/guile/modules/liblogger.so
tests/query/BuggyNotUTest: opencog/guile/libsmob.so
tests/query/BuggyNotUTest: opencog/atoms/foreign/libforeign.so
tests/query/BuggyNotUTest: opencog/persist/prolog/libdatalog.so
tests/query/BuggyNotUTest: opencog/atomspace/libatomspace.so
tests/query/BuggyNotUTest: opencog/atoms/pattern/libpattern.so
tests/query/BuggyNotUTest: opencog/query/libquery-engine.so
tests/query/BuggyNotUTest: opencog/atoms/rule/librule.so
tests/query/BuggyNotUTest: opencog/atoms/execution/libexecution.so
tests/query/BuggyNotUTest: opencog/atoms/reduct/libclearbox.so
tests/query/BuggyNotUTest: opencog/atoms/parallel/libparallel.so
tests/query/BuggyNotUTest: opencog/atoms/flow/libatomflow.so
tests/query/BuggyNotUTest: opencog/atoms/join/libjoin.so
tests/query/BuggyNotUTest: opencog/atoms/core/libatomcore.so
tests/query/BuggyNotUTest: opencog/atoms/grounded/libgrounded.so
tests/query/BuggyNotUTest: opencog/atoms/base/libatombase.so
tests/query/BuggyNotUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/query/BuggyNotUTest: opencog/atoms/value/libvalue.so
tests/query/BuggyNotUTest: opencog/atoms/atom_types/libatom_types.so
tests/query/BuggyNotUTest: /usr/local/lib/libguile-3.0.so
tests/query/BuggyNotUTest: /usr/local/lib/opencog/libcogutil.so
tests/query/BuggyNotUTest: tests/query/CMakeFiles/BuggyNotUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable BuggyNotUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/BuggyNotUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/query/CMakeFiles/BuggyNotUTest.dir/build: tests/query/BuggyNotUTest
.PHONY : tests/query/CMakeFiles/BuggyNotUTest.dir/build

tests/query/CMakeFiles/BuggyNotUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -P CMakeFiles/BuggyNotUTest.dir/cmake_clean.cmake
.PHONY : tests/query/CMakeFiles/BuggyNotUTest.dir/clean

tests/query/CMakeFiles/BuggyNotUTest.dir/depend: tests/query/BuggyNotUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/query /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/query /workspaces/opencog-central/atomspace/build/tests/query/CMakeFiles/BuggyNotUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/query/CMakeFiles/BuggyNotUTest.dir/depend

