# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/atom_types
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/atom_types
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(NameServerUTest "NameServerUTest")
set_tests_properties(NameServerUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/atom_types/CMakeLists.txt;8;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/atom_types/CMakeLists.txt;0;")
add_test(AtomNamesUTest "AtomNamesUTest")
set_tests_properties(AtomNamesUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/atom_types/CMakeLists.txt;9;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/atom_types/CMakeLists.txt;0;")
