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
include tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/flags.make

tests/atoms/execution/DefinedSchemaUTest.cpp: /workspaces/opencog-central/atomspace/tests/atoms/execution/DefinedSchemaUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating DefinedSchemaUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atoms/execution/DefinedSchemaUTest.cpp /workspaces/opencog-central/atomspace/tests/atoms/execution/DefinedSchemaUTest.cxxtest

tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o: tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/flags.make
tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o: tests/atoms/execution/DefinedSchemaUTest.cpp
tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o: tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o -MF CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o.d -o CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atoms/execution/DefinedSchemaUTest.cpp

tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atoms/execution/DefinedSchemaUTest.cpp > CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.i

tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atoms/execution/DefinedSchemaUTest.cpp -o CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.s

# Object files for target DefinedSchemaUTest
DefinedSchemaUTest_OBJECTS = \
"CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o"

# External object files for target DefinedSchemaUTest
DefinedSchemaUTest_EXTERNAL_OBJECTS =

tests/atoms/execution/DefinedSchemaUTest: tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DefinedSchemaUTest.cpp.o
tests/atoms/execution/DefinedSchemaUTest: tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/build.make
tests/atoms/execution/DefinedSchemaUTest: opencog/guile/libsmob.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/foreign/libforeign.so
tests/atoms/execution/DefinedSchemaUTest: opencog/persist/prolog/libdatalog.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atomspace/libatomspace.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/join/libjoin.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/pattern/libpattern.so
tests/atoms/execution/DefinedSchemaUTest: opencog/query/libquery-engine.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/rule/librule.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/grounded/libgrounded.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/execution/libexecution.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/reduct/libclearbox.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/flow/libatomflow.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/parallel/libparallel.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/core/libatomcore.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/base/libatombase.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/value/libvalue.so
tests/atoms/execution/DefinedSchemaUTest: opencog/atoms/atom_types/libatom_types.so
tests/atoms/execution/DefinedSchemaUTest: /usr/local/lib/libguile-3.0.so
tests/atoms/execution/DefinedSchemaUTest: /usr/local/lib/opencog/libcogutil.so
tests/atoms/execution/DefinedSchemaUTest: tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable DefinedSchemaUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DefinedSchemaUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/build: tests/atoms/execution/DefinedSchemaUTest
.PHONY : tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/build

tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/execution && $(CMAKE_COMMAND) -P CMakeFiles/DefinedSchemaUTest.dir/cmake_clean.cmake
.PHONY : tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/clean

tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/depend: tests/atoms/execution/DefinedSchemaUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atoms/execution /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atoms/execution /workspaces/opencog-central/atomspace/build/tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atoms/execution/CMakeFiles/DefinedSchemaUTest.dir/depend

