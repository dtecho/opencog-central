# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/persist/flow
# Build directory: /workspaces/opencog-central/atomspace/build/tests/persist/flow
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(FetchValueOfTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/persist/flow/fetch-value-of-test.scm")
set_tests_properties(FetchValueOfTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/persist/flow" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/flow/CMakeLists.txt;2;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/persist/flow/CMakeLists.txt;0;")
