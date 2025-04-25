# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/parallel
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/parallel
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ParallelUTest "ParallelUTest")
set_tests_properties(ParallelUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/parallel/CMakeLists.txt;3;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/parallel/CMakeLists.txt;0;")
add_test(ThreadedUTest "ThreadedUTest")
set_tests_properties(ThreadedUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/parallel/CMakeLists.txt;5;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/parallel/CMakeLists.txt;0;")
