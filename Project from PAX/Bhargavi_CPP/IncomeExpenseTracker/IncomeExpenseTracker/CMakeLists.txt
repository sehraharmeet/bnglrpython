cmake_minimum_required(VERSION 3.25...3.30)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(MSVC)
    add_compile_options(/W4 /WX)
else()
    add_compile_options(-Wall -Wextra -Wpedantic)
endif()

add_executable(tracker
    src/main.cpp
    src/Tracker.cpp
)

target_include_directories(tracker PRIVATE include)