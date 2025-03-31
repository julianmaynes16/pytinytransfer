# cmake_policy(VERSION 3.5)
cmake_minimum_required(VERSION 3.5)
project(pytinytransfer)

# set(CMAKE_CXX_STANDARD 17)
# set(CMAKE_CXX_STANDARD_REQUIRED ON)
# set(CMAKE_TRY_COMPILE_TARGET_TYPE STATIC_LIBRARY)
# add_compile_definitions(HEATSHRINK_DYNAMIC_ALLOC=0)

add_library(tinytransfer STATIC src/tinyTransfer.cpp)
add_library(heatshrink src/heatshrink/heatshrink_encoder.c src/heatshrink/heatshrink_decoder.c)
target_include_directories(tinytransfer PUBLIC src/)
target_include_directories(heatshrink PUBLIC src/heatshrink)

add_subdirectory(pybind11)
pybind11_add_module(pytinytransfer binder.cpp src/tinyTransfer.cpp)

target_link_libraries(tinytransfer heatshrink)
target_link_libraries(pytinytransfer PRIVATE tinytransfer)
# add_library(heatshrink ${CMAKE_CURRENT_SOURCE_DIR}/src/heatshrink/heatshrink_encoder.c ${CMAKE_CURRENT_SOURCE_DIR}/src/heatshrink/heatshrink_decoder.c)
# add_library(tinytransfer ${CMAKE_CURRENT_SOURCE_DIR}/src/tinytransfer.cpp)
# target_include_directories(heatshrink PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src/heatshrink)
# target_include_directories(tinytransfer PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
# target_compile_options(heatshrink PRIVATE -Wno-unknown-pragmas)
# target_link_libraries(tinytransfer heatshrink)

# target_link_libraries(pytinytransfer tinytransfer)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
target_compile_definitions(pytinytransfer
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
