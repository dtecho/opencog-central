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
include opencog/cython/opencog/CMakeFiles/logger_cython.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include opencog/cython/opencog/CMakeFiles/logger_cython.dir/compiler_depend.make

# Include the progress variables for this target.
include opencog/cython/opencog/CMakeFiles/logger_cython.dir/progress.make

# Include the compile flags for this target's objects.
include opencog/cython/opencog/CMakeFiles/logger_cython.dir/flags.make

opencog/cython/opencog/logger.cpp: /workspaces/opencog-central/atomspace/opencog/cython/opencog/logger.pyx
opencog/cython/opencog/logger.cpp: /workspaces/opencog-central/atomspace/opencog/cython/opencog/logger.pxd
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Cythonizing logger.pyx"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && /usr/bin/cython3 -3 -f -Wextra -I /workspaces/opencog-central/atomspace/build -I /workspaces/opencog-central/atomspace/opencog/cython/opencog -o logger.cpp --cplus /workspaces/opencog-central/atomspace/opencog/cython/opencog/logger.pyx

opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o: opencog/cython/opencog/CMakeFiles/logger_cython.dir/flags.make
opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o: opencog/cython/opencog/logger.cpp
opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o: opencog/cython/opencog/CMakeFiles/logger_cython.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o -MF CMakeFiles/logger_cython.dir/logger.cpp.o.d -o CMakeFiles/logger_cython.dir/logger.cpp.o -c /workspaces/opencog-central/atomspace/build/opencog/cython/opencog/logger.cpp

opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/logger_cython.dir/logger.cpp.i"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /workspaces/opencog-central/atomspace/build/opencog/cython/opencog/logger.cpp > CMakeFiles/logger_cython.dir/logger.cpp.i

opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/logger_cython.dir/logger.cpp.s"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /workspaces/opencog-central/atomspace/build/opencog/cython/opencog/logger.cpp -o CMakeFiles/logger_cython.dir/logger.cpp.s

# Object files for target logger_cython
logger_cython_OBJECTS = \
"CMakeFiles/logger_cython.dir/logger.cpp.o"

# External object files for target logger_cython
logger_cython_EXTERNAL_OBJECTS =

opencog/cython/opencog/logger.so: opencog/cython/opencog/CMakeFiles/logger_cython.dir/logger.cpp.o
opencog/cython/opencog/logger.so: opencog/cython/opencog/CMakeFiles/logger_cython.dir/build.make
opencog/cython/opencog/logger.so: /usr/local/lib/opencog/libcogutil.so
opencog/cython/opencog/logger.so: /usr/lib/x86_64-linux-gnu/libpython3.11.so
opencog/cython/opencog/logger.so: opencog/cython/opencog/CMakeFiles/logger_cython.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/workspaces/opencog-central/atomspace/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared library logger.so"
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/logger_cython.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
opencog/cython/opencog/CMakeFiles/logger_cython.dir/build: opencog/cython/opencog/logger.so
.PHONY : opencog/cython/opencog/CMakeFiles/logger_cython.dir/build

opencog/cython/opencog/CMakeFiles/logger_cython.dir/clean:
	cd /workspaces/opencog-central/atomspace/build/opencog/cython/opencog && $(CMAKE_COMMAND) -P CMakeFiles/logger_cython.dir/cmake_clean.cmake
.PHONY : opencog/cython/opencog/CMakeFiles/logger_cython.dir/clean

opencog/cython/opencog/CMakeFiles/logger_cython.dir/depend: opencog/cython/opencog/logger.cpp
	cd /workspaces/opencog-central/atomspace/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /workspaces/opencog-central/atomspace /workspaces/opencog-central/atomspace/opencog/cython/opencog /workspaces/opencog-central/atomspace/build /workspaces/opencog-central/atomspace/build/opencog/cython/opencog /workspaces/opencog-central/atomspace/build/opencog/cython/opencog/CMakeFiles/logger_cython.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : opencog/cython/opencog/CMakeFiles/logger_cython.dir/depend

