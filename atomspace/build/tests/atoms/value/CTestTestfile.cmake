# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/value
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/value
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ValueUTest "ValueUTest")
set_tests_properties(ValueUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;8;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;0;")
add_test(StreamUTest "StreamUTest")
set_tests_properties(StreamUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;10;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;0;")
add_test(VoidValueUTest "VoidValueUTest")
set_tests_properties(VoidValueUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;13;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/value/CMakeLists.txt;0;")
