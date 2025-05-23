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
include tests/query/CMakeFiles/SudokuUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/query/CMakeFiles/SudokuUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/query/CMakeFiles/SudokuUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/query/CMakeFiles/SudokuUTest.dir/flags.make

tests/query/SudokuUTest.cpp: /workspaces/opencog-central/atomspace/tests/query/SudokuUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating SudokuUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/query/SudokuUTest.cpp /workspaces/opencog-central/atomspace/tests/query/SudokuUTest.cxxtest

tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o: tests/query/CMakeFiles/SudokuUTest.dir/flags.make
tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o: tests/query/SudokuUTest.cpp
tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o: tests/query/CMakeFiles/SudokuUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o -MF CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o.d -o CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/query/SudokuUTest.cpp

tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/query/SudokuUTest.cpp > CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.i

tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/query/SudokuUTest.cpp -o CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.s

# Object files for target SudokuUTest
SudokuUTest_OBJECTS = \
"CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o"

# External object files for target SudokuUTest
SudokuUTest_EXTERNAL_OBJECTS =

tests/query/SudokuUTest: tests/query/CMakeFiles/SudokuUTest.dir/SudokuUTest.cpp.o
tests/query/SudokuUTest: tests/query/CMakeFiles/SudokuUTest.dir/build.make
tests/query/SudokuUTest: opencog/guile/modules/liblogger.so
tests/query/SudokuUTest: opencog/guile/libsmob.so
tests/query/SudokuUTest: opencog/atoms/foreign/libforeign.so
tests/query/SudokuUTest: opencog/persist/prolog/libdatalog.so
tests/query/SudokuUTest: opencog/atomspace/libatomspace.so
tests/query/SudokuUTest: opencog/atoms/pattern/libpattern.so
tests/query/SudokuUTest: opencog/query/libquery-engine.so
tests/query/SudokuUTest: opencog/atoms/rule/librule.so
tests/query/SudokuUTest: opencog/atoms/execution/libexecution.so
tests/query/SudokuUTest: opencog/atoms/reduct/libclearbox.so
tests/query/SudokuUTest: opencog/atoms/parallel/libparallel.so
tests/query/SudokuUTest: opencog/atoms/flow/libatomflow.so
tests/query/SudokuUTest: opencog/atoms/join/libjoin.so
tests/query/SudokuUTest: opencog/atoms/core/libatomcore.so
tests/query/SudokuUTest: opencog/atoms/grounded/libgrounded.so
tests/query/SudokuUTest: opencog/atoms/base/libatombase.so
tests/query/SudokuUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/query/SudokuUTest: opencog/atoms/value/libvalue.so
tests/query/SudokuUTest: opencog/atoms/atom_types/libatom_types.so
tests/query/SudokuUTest: /usr/local/lib/libguile-3.0.so
tests/query/SudokuUTest: /usr/local/lib/opencog/libcogutil.so
tests/query/SudokuUTest: tests/query/CMakeFiles/SudokuUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable SudokuUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/SudokuUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/query/CMakeFiles/SudokuUTest.dir/build: tests/query/SudokuUTest
.PHONY : tests/query/CMakeFiles/SudokuUTest.dir/build

tests/query/CMakeFiles/SudokuUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -P CMakeFiles/SudokuUTest.dir/cmake_clean.cmake
.PHONY : tests/query/CMakeFiles/SudokuUTest.dir/clean

tests/query/CMakeFiles/SudokuUTest.dir/depend: tests/query/SudokuUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/query /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/query /workspaces/opencog-central/atomspace/build/tests/query/CMakeFiles/SudokuUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/query/CMakeFiles/SudokuUTest.dir/depend

