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
include tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/compiler_depend.make

# Include the progress variables for this target.
include tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/progress.make

# Include the compile flags for this target's objects.
include tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/flags.make

tests/persist/sexpr/DispatchUTest.cpp: /workspaces/opencog-central/atomspace/tests/persist/sexpr/DispatchUTest.cxxtest
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating DispatchUTest.cpp"
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && /usr/bin/cxxtestgen --runner=ErrorPrinter --have-eh -o /workspaces/opencog-central/atomspace/build/tests/persist/sexpr/DispatchUTest.cpp /workspaces/opencog-central/atomspace/tests/persist/sexpr/DispatchUTest.cxxtest

tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o: tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/flags.make
tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o: tests/persist/sexpr/DispatchUTest.cpp
tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o: tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o -MF CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o.d -o CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o -c /workspaces/opencog-central/atomspace/build/tests/persist/sexpr/DispatchUTest.cpp

tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/tests/persist/sexpr/DispatchUTest.cpp > CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.i

tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/tests/persist/sexpr/DispatchUTest.cpp -o CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.s

# Object files for target DispatchUTest
DispatchUTest_OBJECTS = \
"CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o"

# External object files for target DispatchUTest
DispatchUTest_EXTERNAL_OBJECTS =

tests/persist/sexpr/DispatchUTest: tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DispatchUTest.cpp.o
tests/persist/sexpr/DispatchUTest: tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/build.make
tests/persist/sexpr/DispatchUTest: opencog/persist/file/libload_scm.so
tests/persist/sexpr/DispatchUTest: opencog/persist/sexcom/libsexcom.so
tests/persist/sexpr/DispatchUTest: opencog/persist/proxy/libpersist-proxy.so
tests/persist/sexpr/DispatchUTest: opencog/persist/api/libpersist.so
tests/persist/sexpr/DispatchUTest: opencog/persist/storage/libstorage-types.so
tests/persist/sexpr/DispatchUTest: opencog/guile/libsmob.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/foreign/libforeign.so
tests/persist/sexpr/DispatchUTest: opencog/persist/prolog/libdatalog.so
tests/persist/sexpr/DispatchUTest: /usr/local/lib/libguile-3.0.so
tests/persist/sexpr/DispatchUTest: opencog/persist/sexpr/libsexpr.so
tests/persist/sexpr/DispatchUTest: opencog/atomspace/libatomspace.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/join/libjoin.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/pattern/libpattern.so
tests/persist/sexpr/DispatchUTest: opencog/query/libquery-engine.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/rule/librule.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/grounded/libgrounded.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/execution/libexecution.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/reduct/libclearbox.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/parallel/libparallel.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/flow/libatomflow.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/core/libatomcore.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/base/libatombase.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/truthvalue/libtruthvalue.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/value/libvalue.so
tests/persist/sexpr/DispatchUTest: opencog/atoms/atom_types/libatom_types.so
tests/persist/sexpr/DispatchUTest: /usr/local/lib/opencog/libcogutil.so
tests/persist/sexpr/DispatchUTest: tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable DispatchUTest"
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DispatchUTest.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/build: tests/persist/sexpr/DispatchUTest
.PHONY : tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/build

tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/tests/persist/sexpr && $(CMAKE_COMMAND) -P CMakeFiles/DispatchUTest.dir/cmake_clean.cmake
.PHONY : tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/clean

tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/depend: tests/persist/sexpr/DispatchUTest.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/tests/persist/sexpr /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/tests/persist/sexpr /workspaces/opencog-central/atomspace/build/tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : tests/persist/sexpr/CMakeFiles/DispatchUTest.dir/depend

