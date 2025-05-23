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
include tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/flags.make

tests/atoms/reduct/MinMaxUTest.cpp: /workspaces/opencog-central/atomspace/tests/atoms/reduct/MinMaxUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating MinMaxUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atoms/reduct/MinMaxUTest.cpp /workspaces/opencog-central/atomspace/tests/atoms/reduct/MinMaxUTest.cxxtest

tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o: tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/flags.make
tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o: tests/atoms/reduct/MinMaxUTest.cpp
tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o: tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o -MF CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o.d -o CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atoms/reduct/MinMaxUTest.cpp

tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atoms/reduct/MinMaxUTest.cpp > CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.i

tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atoms/reduct/MinMaxUTest.cpp -o CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.s

# Object files for target MinMaxUTest
MinMaxUTest_OBJECTS = \
"CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o"

# External object files for target MinMaxUTest
MinMaxUTest_EXTERNAL_OBJECTS =

tests/atoms/reduct/MinMaxUTest: tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/MinMaxUTest.cpp.o
tests/atoms/reduct/MinMaxUTest: tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/build.make
tests/atoms/reduct/MinMaxUTest: opencog/guile/libsmob.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/foreign/libforeign.so
tests/atoms/reduct/MinMaxUTest: opencog/persist/prolog/libdatalog.so
tests/atoms/reduct/MinMaxUTest: opencog/atomspace/libatomspace.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/join/libjoin.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/pattern/libpattern.so
tests/atoms/reduct/MinMaxUTest: opencog/query/libquery-engine.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/rule/librule.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/grounded/libgrounded.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/execution/libexecution.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/reduct/libclearbox.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/flow/libatomflow.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/parallel/libparallel.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/core/libatomcore.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/base/libatombase.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/value/libvalue.so
tests/atoms/reduct/MinMaxUTest: opencog/atoms/atom_types/libatom_types.so
tests/atoms/reduct/MinMaxUTest: /usr/local/lib/libguile-3.0.so
tests/atoms/reduct/MinMaxUTest: /usr/local/lib/opencog/libcogutil.so
tests/atoms/reduct/MinMaxUTest: tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable MinMaxUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MinMaxUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/build: tests/atoms/reduct/MinMaxUTest
.PHONY : tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/build

tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/reduct && $(CMAKE_COMMAND) -P CMakeFiles/MinMaxUTest.dir/cmake_clean.cmake
.PHONY : tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/clean

tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/depend: tests/atoms/reduct/MinMaxUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atoms/reduct /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atoms/reduct /workspaces/opencog-central/atomspace/build/tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atoms/reduct/CMakeFiles/MinMaxUTest.dir/depend

