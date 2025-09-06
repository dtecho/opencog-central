
# Source files
set(RWKV_CPP_SOURCES
    rwkv_wrapper.cpp
    text_generator.cpp
    utils.cpp
)

# Create static library
add_library(rwkv_cpp_static STATIC ${RWKV_CPP_SOURCES})
target_link_libraries(rwkv_cpp_static 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../3p/rwkv.cpp/librwkv.a
    Threads::Threads
)

# Create shared library
add_library(rwkv_cpp_shared SHARED ${RWKV_CPP_SOURCES})
target_link_libraries(rwkv_cpp_shared 
    ${CMAKE_CURRENT_SOURCE_DIR}/../../3p/rwkv.cpp/librwkv.a
    Threads::Threads
)

# Set library properties
set_target_properties(rwkv_cpp_static PROPERTIES
    OUTPUT_NAME rwkv_cpp
    PREFIX "lib"
)

set_target_properties(rwkv_cpp_shared PROPERTIES
    OUTPUT_NAME rwkv_cpp
    PREFIX "lib"
    VERSION ${PROJECT_VERSION}
    SOVERSION ${PROJECT_VERSION_MAJOR}
)

# Install targets
install(TARGETS rwkv_cpp_static rwkv_cpp_shared
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)
