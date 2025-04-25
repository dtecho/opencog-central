# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/atoms/truthvalue
# Build directory: /workspaces/opencog-central/atomspace/build/tests/atoms/truthvalue
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(SimpleTruthValueUTest "SimpleTruthValueUTest")
set_tests_properties(SimpleTruthValueUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;8;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;0;")
add_test(TVUTest "TVUTest")
set_tests_properties(TVUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;9;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;0;")
add_test(TVMergeUTest "TVMergeUTest")
set_tests_properties(TVMergeUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;10;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;0;")
add_test(EvidenceCountTruthValueUTest "EvidenceCountTruthValueUTest")
set_tests_properties(EvidenceCountTruthValueUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;11;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/atoms/truthvalue/CMakeLists.txt;0;")
