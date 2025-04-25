# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/foreign
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/foreign
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(SexprQueryTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/atoms/foreign/sexpr-query-test.scm")
set_tests_properties(SexprQueryTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/atoms/foreign" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/foreign/CMakeLists.txt;4;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/atoms/foreign/CMakeLists.txt;0;")
add_test(DatalogBasicTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/atoms/foreign/datalog-basic-test.scm")
set_tests_properties(DatalogBasicTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/atoms/foreign" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/foreign/CMakeLists.txt;5;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/atoms/foreign/CMakeLists.txt;0;")
