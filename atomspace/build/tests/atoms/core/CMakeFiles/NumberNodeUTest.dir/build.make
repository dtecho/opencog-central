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
include tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/flags.make

tests/atoms/core/NumberNodeUTest.cpp: /workspaces/opencog-central/atomspace/tests/atoms/core/NumberNodeUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating NumberNodeUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atoms/core/NumberNodeUTest.cpp /workspaces/opencog-central/atomspace/tests/atoms/core/NumberNodeUTest.cxxtest

tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o: tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/flags.make
tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o: tests/atoms/core/NumberNodeUTest.cpp
tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o: tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o -MF CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o.d -o CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atoms/core/NumberNodeUTest.cpp

tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atoms/core/NumberNodeUTest.cpp > CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.i

tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atoms/core/NumberNodeUTest.cpp -o CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.s

# Object files for target NumberNodeUTest
NumberNodeUTest_OBJECTS = \
"CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o"

# External object files for target NumberNodeUTest
NumberNodeUTest_EXTERNAL_OBJECTS =

tests/atoms/core/NumberNodeUTest: tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/NumberNodeUTest.cpp.o
tests/atoms/core/NumberNodeUTest: tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/build.make
tests/atoms/core/NumberNodeUTest: opencog/guile/libsmob.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/foreign/libforeign.so
tests/atoms/core/NumberNodeUTest: opencog/persist/prolog/libdatalog.so
tests/atoms/core/NumberNodeUTest: opencog/atomspace/libatomspace.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/join/libjoin.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/pattern/libpattern.so
tests/atoms/core/NumberNodeUTest: opencog/query/libquery-engine.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/rule/librule.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/grounded/libgrounded.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/execution/libexecution.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/reduct/libclearbox.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/flow/libatomflow.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/parallel/libparallel.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/core/libatomcore.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/base/libatombase.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/value/libvalue.so
tests/atoms/core/NumberNodeUTest: opencog/atoms/atom_types/libatom_types.so
tests/atoms/core/NumberNodeUTest: /usr/local/lib/libguile-3.0.so
tests/atoms/core/NumberNodeUTest: /usr/local/lib/opencog/libcogutil.so
tests/atoms/core/NumberNodeUTest: tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable NumberNodeUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/NumberNodeUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/build: tests/atoms/core/NumberNodeUTest
.PHONY : tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/build

tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/core && $(CMAKE_COMMAND) -P CMakeFiles/NumberNodeUTest.dir/cmake_clean.cmake
.PHONY : tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/clean

tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/depend: tests/atoms/core/NumberNodeUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atoms/core /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atoms/core /workspaces/opencog-central/atomspace/build/tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atoms/core/CMakeFiles/NumberNodeUTest.dir/depend

