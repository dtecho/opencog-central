# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/rule
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/rule
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(RuleTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/atoms/rule/rule-test.scm")
set_tests_properties(RuleTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/atoms/rule" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/rule/CMakeLists.txt;4;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/atoms/rule/CMakeLists.txt;0;")
