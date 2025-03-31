# cmake_policy(VERSION 3.5)
cmake_minimum_required(VERSION 3.5)
project(pytinytransfer)

add_library(tinytransfer STATIC src/tinytransfer/tinyTransfer.cpp)
add_library(heatshrink src/tinytransfer/heatshrink/heatshrink_encoder.c src/tinytransfer/heatshrink/heatshrink_decoder.c)
target_include_directories(tinytransfer PUBLIC src/tinytransfer)
target_include_directories(heatshrink PUBLIC src/tinytransfer/heatshrink)

add_subdirectory(pybind11)
pybind11_add_module(pytinytransfer binder.cpp src/tinytransfer/tinyTransfer.cpp)

target_link_libraries(tinytransfer heatshrink)
target_link_libraries(pytinytransfer PRIVATE tinytransfer)

target_compile_definitions(pytinytransfer
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
