# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/pattern
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/pattern
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(BindLinkUTest "BindLinkUTest")
set_tests_properties(BindLinkUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;7;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;0;")
add_test(SatisfactionLinkUTest "SatisfactionLinkUTest")
set_tests_properties(SatisfactionLinkUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;8;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;0;")
add_test(PatternUtilsUTest "PatternUtilsUTest")
set_tests_properties(PatternUtilsUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;9;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/pattern/CMakeLists.txt;0;")
