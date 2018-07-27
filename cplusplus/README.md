C/Cplusplus
=====

GCC  
---

GCC 原名为 GNU C 语言编译器（GNU C Compiler），因为它原本只能处理 C语言。GCC 很快地扩展，变得可处理 C++。后来又扩展能够支持更多编程语言，如Fortran、Pascal、Objective-C、Java、Ada、Go以及各类处理器架构上的汇编语言等，所以改名GNU编译器套件（GNU Compiler Collection）。

1. 编译参数简介

    1.-I:增加头文件搜索路劲
    ```sh
        gcc -I /usr/include/python3.5m/
    ```
    2.-c:生成.o文件
    3.-o:指定生成的文件名
    4.-shared -fPIC: 生成动态库.so文件

2. 例子  
    使用Cython(pip install Cython)加密py文件,生成python可以使用的.so文件,完成加密.  

    1.目标文件 test.py 使用cython生成.c文件

    ```sh
    cython test.py
    ```
    2.编译.c文件
    ```
    gcc -c -fPIC -I/usr/include/python3.5m/ test.c
    gcc -shared test.o -o test.so
    ```
    或者
    ```sh
    gcc -shared -fPIC -I/usr/include/python3.5m/ test.c -o test.so
    ```
    3.去掉so文件中的变量名等...
    ```sh
    strip -s test.so
    ```
    4.检查
    ```sh
    strings test.so
    ```

g++
---

GNU的c++编译器  

1. cplusplus编译参数简介  
    --std=c++17:使用c++17进行编译
