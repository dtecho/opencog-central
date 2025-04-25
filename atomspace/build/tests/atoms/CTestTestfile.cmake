# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(HashUTest "HashUTest")
set_tests_properties(HashUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;23;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;0;")
add_test(RandomUTest "RandomUTest")
set_tests_properties(RandomUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;24;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;0;")
add_test(AlphaConvertUTest "AlphaConvertUTest")
set_tests_properties(AlphaConvertUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;25;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;0;")
add_test(BetaReduceUTest "BetaReduceUTest")
set_tests_properties(BetaReduceUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;26;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/CMakeLists.txt;0;")
subdirs("atom_types")
subdirs("base")
subdirs("core")
subdirs("evaluation")
subdirs("execution")
subdirs("rule")
subdirs("join")
subdirs("parallel")
subdirs("truthvalue")
subdirs("value")
subdirs("reduct")
subdirs("flow")
subdirs("pattern")
subdirs("foreign")
