cmake_minimum_required(VERSION 3.12)
project(SwarmEngineCPP)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Executable for high-performance pathfinding engine
add_executable(pathfinding_engine pathfinding_engine.cpp)
