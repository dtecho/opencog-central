# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/persist/sexpr
# Build directory: /workspaces/opencog-central/atomspace/build/tests/persist/sexpr
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(FastLoadUTest "FastLoadUTest")
set_tests_properties(FastLoadUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;3;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;0;")
add_test(CommandsUTest "CommandsUTest")
set_tests_properties(CommandsUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;4;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;0;")
add_test(DispatchUTest "DispatchUTest")
set_tests_properties(DispatchUTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" _BACKTRACE_TRIPLES "/usr/local/share/opencog/cmake/AddCxxtest.cmake;36;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;5;ADD_CXXTEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;0;")
add_test(FileStorageTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/persist/sexpr/file-storage.scm")
set_tests_properties(FileStorageTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/persist/sexpr" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;7;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;0;")
add_test(FileEpisodicTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/persist/sexpr/file-episodic.scm")
set_tests_properties(FileEpisodicTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/persist/sexpr" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;8;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/persist/sexpr/CMakeLists.txt;0;")
