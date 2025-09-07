set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS_DEBUG "-g3 -ggdb")
cmake_minimum_required(VERSION 3.5)

set(TINYTRANSFER_X86 1)

add_subdirectory(tinytransfer)
add_subdirectory(pybind11)

pybind11_add_module(pytinytransfer binder.cpp)
target_link_libraries(pytinytransfer PRIVATE tinytransfer)

target_compile_definitions(pytinytransfer PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
