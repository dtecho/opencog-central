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
include tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/flags.make

tests/atoms/join/JoinLinkUTest.cpp: /workspaces/opencog-central/atomspace/tests/atoms/join/JoinLinkUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating JoinLinkUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atoms/join/JoinLinkUTest.cpp /workspaces/opencog-central/atomspace/tests/atoms/join/JoinLinkUTest.cxxtest

tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o: tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/flags.make
tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o: tests/atoms/join/JoinLinkUTest.cpp
tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o: tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o -MF CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o.d -o CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atoms/join/JoinLinkUTest.cpp

tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atoms/join/JoinLinkUTest.cpp > CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.i

tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atoms/join/JoinLinkUTest.cpp -o CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.s

# Object files for target JoinLinkUTest
JoinLinkUTest_OBJECTS = \
"CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o"

# External object files for target JoinLinkUTest
JoinLinkUTest_EXTERNAL_OBJECTS =

tests/atoms/join/JoinLinkUTest: tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/JoinLinkUTest.cpp.o
tests/atoms/join/JoinLinkUTest: tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/build.make
tests/atoms/join/JoinLinkUTest: opencog/guile/libsmob.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/foreign/libforeign.so
tests/atoms/join/JoinLinkUTest: opencog/persist/prolog/libdatalog.so
tests/atoms/join/JoinLinkUTest: opencog/atomspace/libatomspace.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/join/libjoin.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/pattern/libpattern.so
tests/atoms/join/JoinLinkUTest: opencog/query/libquery-engine.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/rule/librule.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/grounded/libgrounded.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/execution/libexecution.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/reduct/libclearbox.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/flow/libatomflow.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/parallel/libparallel.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/core/libatomcore.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/base/libatombase.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/value/libvalue.so
tests/atoms/join/JoinLinkUTest: opencog/atoms/atom_types/libatom_types.so
tests/atoms/join/JoinLinkUTest: /usr/local/lib/libguile-3.0.so
tests/atoms/join/JoinLinkUTest: /usr/local/lib/opencog/libcogutil.so
tests/atoms/join/JoinLinkUTest: tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable JoinLinkUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/JoinLinkUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/build: tests/atoms/join/JoinLinkUTest
.PHONY : tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/build

tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/join && $(CMAKE_COMMAND) -P CMakeFiles/JoinLinkUTest.dir/cmake_clean.cmake
.PHONY : tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/clean

tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/depend: tests/atoms/join/JoinLinkUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atoms/join /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atoms/join /workspaces/opencog-central/atomspace/build/tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atoms/join/CMakeFiles/JoinLinkUTest.dir/depend

