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
include tests/query/CMakeFiles/IllPutUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/query/CMakeFiles/IllPutUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/query/CMakeFiles/IllPutUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/query/CMakeFiles/IllPutUTest.dir/flags.make

tests/query/IllPutUTest.cpp: /workspaces/opencog-central/atomspace/tests/query/IllPutUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating IllPutUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/query/IllPutUTest.cpp /workspaces/opencog-central/atomspace/tests/query/IllPutUTest.cxxtest

tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o: tests/query/CMakeFiles/IllPutUTest.dir/flags.make
tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o: tests/query/IllPutUTest.cpp
tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o: tests/query/CMakeFiles/IllPutUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o -MF CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o.d -o CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/query/IllPutUTest.cpp

tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/query/IllPutUTest.cpp > CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.i

tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/query && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/query/IllPutUTest.cpp -o CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.s

# Object files for target IllPutUTest
IllPutUTest_OBJECTS = \
"CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o"

# External object files for target IllPutUTest
IllPutUTest_EXTERNAL_OBJECTS =

tests/query/IllPutUTest: tests/query/CMakeFiles/IllPutUTest.dir/IllPutUTest.cpp.o
tests/query/IllPutUTest: tests/query/CMakeFiles/IllPutUTest.dir/build.make
tests/query/IllPutUTest: opencog/guile/modules/liblogger.so
tests/query/IllPutUTest: opencog/guile/libsmob.so
tests/query/IllPutUTest: opencog/atoms/foreign/libforeign.so
tests/query/IllPutUTest: opencog/persist/prolog/libdatalog.so
tests/query/IllPutUTest: opencog/atomspace/libatomspace.so
tests/query/IllPutUTest: opencog/atoms/pattern/libpattern.so
tests/query/IllPutUTest: opencog/query/libquery-engine.so
tests/query/IllPutUTest: opencog/atoms/rule/librule.so
tests/query/IllPutUTest: opencog/atoms/execution/libexecution.so
tests/query/IllPutUTest: opencog/atoms/reduct/libclearbox.so
tests/query/IllPutUTest: opencog/atoms/parallel/libparallel.so
tests/query/IllPutUTest: opencog/atoms/flow/libatomflow.so
tests/query/IllPutUTest: opencog/atoms/join/libjoin.so
tests/query/IllPutUTest: opencog/atoms/core/libatomcore.so
tests/query/IllPutUTest: opencog/atoms/grounded/libgrounded.so
tests/query/IllPutUTest: opencog/atoms/base/libatombase.so
tests/query/IllPutUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/query/IllPutUTest: opencog/atoms/value/libvalue.so
tests/query/IllPutUTest: opencog/atoms/atom_types/libatom_types.so
tests/query/IllPutUTest: /usr/local/lib/libguile-3.0.so
tests/query/IllPutUTest: /usr/local/lib/opencog/libcogutil.so
tests/query/IllPutUTest: tests/query/CMakeFiles/IllPutUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable IllPutUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/IllPutUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/query/CMakeFiles/IllPutUTest.dir/build: tests/query/IllPutUTest
.PHONY : tests/query/CMakeFiles/IllPutUTest.dir/build

tests/query/CMakeFiles/IllPutUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/query && $(CMAKE_COMMAND) -P CMakeFiles/IllPutUTest.dir/cmake_clean.cmake
.PHONY : tests/query/CMakeFiles/IllPutUTest.dir/clean

tests/query/CMakeFiles/IllPutUTest.dir/depend: tests/query/IllPutUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/query /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/query /workspaces/opencog-central/atomspace/build/tests/query/CMakeFiles/IllPutUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/query/CMakeFiles/IllPutUTest.dir/depend

