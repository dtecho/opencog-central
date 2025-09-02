
cmake_minimum_required(VERSION 3.18)
project(KoboldCpp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add the existing KoboldCpp directory
add_subdirectory(${CMAKE_SOURCE_DIR}/3p/koboldcpp koboldcpp_build)

# Create our integration wrapper
add_executable(koboldcpp_server
    src/main.cpp
    src/kogserver_bridge.cpp
)

target_include_directories(koboldcpp_server PRIVATE
    ${CMAKE_SOURCE_DIR}/3p/koboldcpp
    ${CMAKE_SOURCE_DIR}/atomspace/opencog/atomspace
    include
)

target_link_libraries(koboldcpp_server
    ${CMAKE_SOURCE_DIR}/3p/koboldcpp/koboldcpp_default.so
)
