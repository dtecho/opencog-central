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
include tests/query/CMakeFiles/TypeChoiceUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/query/CMakeFiles/TypeChoiceUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/query/CMakeFiles/TypeChoiceUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/query/CMakeFiles/TypeChoiceUTest.dir/flags.make

tests/query/TypeChoiceUTest.cpp: /workspaces/opencog-central/atomspace/tests/query/TypeChoiceUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating TypeChoiceUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/query/TypeChoiceUTest.cpp /workspaces/opencog-central/atomspace/tests/query/TypeChoiceUTest.cxxtest

tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o: tests/query/CMakeFiles/TypeChoiceUTest.dir/flags.make
tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o: tests/query/TypeChoiceUTest.cpp
tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o: tests/query/CMakeFiles/TypeChoiceUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o -MF CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o.d -o CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/query/TypeChoiceUTest.cpp

tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/query/TypeChoiceUTest.cpp > CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.i

tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/query/TypeChoiceUTest.cpp -o CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.s

# Object files for target TypeChoiceUTest
TypeChoiceUTest_OBJECTS = \
"CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o"

# External object files for target TypeChoiceUTest
TypeChoiceUTest_EXTERNAL_OBJECTS =

tests/query/TypeChoiceUTest: tests/query/CMakeFiles/TypeChoiceUTest.dir/TypeChoiceUTest.cpp.o
tests/query/TypeChoiceUTest: tests/query/CMakeFiles/TypeChoiceUTest.dir/build.make
tests/query/TypeChoiceUTest: opencog/guile/modules/liblogger.so
tests/query/TypeChoiceUTest: opencog/guile/libsmob.so
tests/query/TypeChoiceUTest: opencog/atoms/foreign/libforeign.so
tests/query/TypeChoiceUTest: opencog/persist/prolog/libdatalog.so
tests/query/TypeChoiceUTest: opencog/atomspace/libatomspace.so
tests/query/TypeChoiceUTest: opencog/atoms/pattern/libpattern.so
tests/query/TypeChoiceUTest: opencog/query/libquery-engine.so
tests/query/TypeChoiceUTest: opencog/atoms/rule/librule.so
tests/query/TypeChoiceUTest: opencog/atoms/execution/libexecution.so
tests/query/TypeChoiceUTest: opencog/atoms/reduct/libclearbox.so
tests/query/TypeChoiceUTest: opencog/atoms/parallel/libparallel.so
tests/query/TypeChoiceUTest: opencog/atoms/flow/libatomflow.so
tests/query/TypeChoiceUTest: opencog/atoms/join/libjoin.so
tests/query/TypeChoiceUTest: opencog/atoms/core/libatomcore.so
tests/query/TypeChoiceUTest: opencog/atoms/grounded/libgrounded.so
tests/query/TypeChoiceUTest: opencog/atoms/base/libatombase.so
tests/query/TypeChoiceUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/query/TypeChoiceUTest: opencog/atoms/value/libvalue.so
tests/query/TypeChoiceUTest: opencog/atoms/atom_types/libatom_types.so
tests/query/TypeChoiceUTest: /usr/local/lib/libguile-3.0.so
tests/query/TypeChoiceUTest: /usr/local/lib/opencog/libcogutil.so
tests/query/TypeChoiceUTest: tests/query/CMakeFiles/TypeChoiceUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable TypeChoiceUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/TypeChoiceUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/query/CMakeFiles/TypeChoiceUTest.dir/build: tests/query/TypeChoiceUTest
.PHONY : tests/query/CMakeFiles/TypeChoiceUTest.dir/build

tests/query/CMakeFiles/TypeChoiceUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -P CMakeFiles/TypeChoiceUTest.dir/cmake_clean.cmake
.PHONY : tests/query/CMakeFiles/TypeChoiceUTest.dir/clean

tests/query/CMakeFiles/TypeChoiceUTest.dir/depend: tests/query/TypeChoiceUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/query /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/query /workspaces/opencog-central/atomspace/build/tests/query/CMakeFiles/TypeChoiceUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/query/CMakeFiles/TypeChoiceUTest.dir/depend

