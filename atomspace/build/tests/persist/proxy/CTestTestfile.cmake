# CMake generated Testfile for 
# Source directory: /workspaces/opencog-central/atomspace/tests/persist/proxy
# Build directory: /workspaces/opencog-central/atomspace/build/tests/persist/proxy
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(ProxyNodeTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/persist/proxy/proxy-node-test.scm")
set_tests_properties(ProxyNodeTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/persist/proxy" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/proxy/CMakeLists.txt;2;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/persist/proxy/CMakeLists.txt;0;")
add_test(ReadProxyTest "guile" "-L" "/workspaces/opencog-central/atomspace/build/opencog/scm" "--use-srfi=64" "/workspaces/opencog-central/atomspace/tests/persist/proxy/read-proxy-test.scm")
set_tests_properties(ReadProxyTest PROPERTIES  ENVIRONMENT "GUILE_LOAD_PATH=/workspaces/opencog-central/atomspace/build/opencog/scm" WORKING_DIRECTORY "/workspaces/opencog-central/atomspace/build/tests/persist/proxy" _BACKTRACE_TRIPLES "/workspaces/opencog-central/atomspace/cmake/OpenCogGuile.cmake;332;ADD_TEST;/workspaces/opencog-central/atomspace/tests/persist/proxy/CMakeLists.txt;3;ADD_GUILE_TEST;/workspaces/opencog-central/atomspace/tests/persist/proxy/CMakeLists.txt;0;")
