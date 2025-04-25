# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/matrix
# Build directory: /workspaces/opencog-central/atomspace/build/tests/matrix
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(VectorAPIUTest "VectorAPIUTest")
set_tests_properties(VectorAPIUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/matrix/CMakeLists.txt;20;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/matrix/CMakeLists.txt;0;")
add_test(MarginalTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/matrix/marginal-test.scm")
set_tests_properties(MarginalTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/matrix" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/matrix/CMakeLists.txt;22;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/matrix/CMakeLists.txt;0;")
