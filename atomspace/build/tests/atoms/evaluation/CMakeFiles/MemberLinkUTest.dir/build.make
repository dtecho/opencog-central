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
include tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/flags.make

tests/atoms/evaluation/MemberLinkUTest.cpp: /workspaces/opencog-central/atomspace/tests/atoms/evaluation/MemberLinkUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating MemberLinkUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/MemberLinkUTest.cpp /workspaces/opencog-central/atomspace/tests/atoms/evaluation/MemberLinkUTest.cxxtest

tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o: tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/flags.make
tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o: tests/atoms/evaluation/MemberLinkUTest.cpp
tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o: tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o -MF CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o.d -o CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/MemberLinkUTest.cpp

tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/MemberLinkUTest.cpp > CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.i

tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/MemberLinkUTest.cpp -o CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.s

# Object files for target MemberLinkUTest
MemberLinkUTest_OBJECTS = \
"CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o"

# External object files for target MemberLinkUTest
MemberLinkUTest_EXTERNAL_OBJECTS =

tests/atoms/evaluation/MemberLinkUTest: tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/MemberLinkUTest.cpp.o
tests/atoms/evaluation/MemberLinkUTest: tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/build.make
tests/atoms/evaluation/MemberLinkUTest: opencog/guile/libsmob.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/foreign/libforeign.so
tests/atoms/evaluation/MemberLinkUTest: opencog/persist/prolog/libdatalog.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atomspace/libatomspace.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/join/libjoin.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/pattern/libpattern.so
tests/atoms/evaluation/MemberLinkUTest: opencog/query/libquery-engine.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/rule/librule.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/grounded/libgrounded.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/execution/libexecution.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/reduct/libclearbox.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/flow/libatomflow.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/parallel/libparallel.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/core/libatomcore.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/base/libatombase.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/value/libvalue.so
tests/atoms/evaluation/MemberLinkUTest: opencog/atoms/atom_types/libatom_types.so
tests/atoms/evaluation/MemberLinkUTest: /usr/local/lib/libguile-3.0.so
tests/atoms/evaluation/MemberLinkUTest: /usr/local/lib/opencog/libcogutil.so
tests/atoms/evaluation/MemberLinkUTest: tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable MemberLinkUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MemberLinkUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/build: tests/atoms/evaluation/MemberLinkUTest
.PHONY : tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/build

tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation && $(CMAKE_COMMAND) -P CMakeFiles/MemberLinkUTest.dir/cmake_clean.cmake
.PHONY : tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/clean

tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/depend: tests/atoms/evaluation/MemberLinkUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/atoms/evaluation /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation /workspaces/opencog-central/atomspace/build/tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/atoms/evaluation/CMakeFiles/MemberLinkUTest.dir/depend

