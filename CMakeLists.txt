cmake_minimum_required(VERSION 3.10)


# 设置项目名称和版本
project(MocapDemo VERSION 1.0)



# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_COMPILER "clang")

# 添加-fdeclspec编译器选项
add_compile_options(-fdeclspec)

# 包含头文件目录
include_directories(${PROJECT_SOURCE_DIR}/include)

# 查找源文件
file(GLOB_RECURSE SOURCES "${PROJECT_SOURCE_DIR}/src/*.cpp")

# 添加可执行文件
add_executable(MyExecutable ${PROJECT_SOURCE_DIR}/main.cpp ${SOURCES})

# 设置输出目录
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/dist)

# 添加库目录（如果有）


# 添加库目录（如果有）
link_directories(${PROJECT_SOURCE_DIR}/lib)

# 链接库（如果有）
# target_link_libraries(MyExecutable <library_name>)


# 为 Clang 编译器添加编译选项
if (CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    target_compile_options(MyExecutable PRIVATE -fdeclspec -fms-extensions)
endif()