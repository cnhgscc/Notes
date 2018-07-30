BOOST
=====

BOOST.PYTHON文档  https://www.boost.org/doc/libs/1_67_0/libs/python/doc/html/index.html

ubuntu 安装
----------

sudo apt install libboost-all-dev

编译例子
------

1. python2

    g++ hello_ext.cpp -o hello_ext.so -I /usr/lib -I /usr/include/boost -I /usr/include/python2.7 -shared -fPIC -std=c++11  -lboost_python

2. python3

    1. cd /usr/lib/x86_64-linux-gnu/  
    2. sudo ln -s libboost_python-py35.so libboost_python3.so  

    g++ hello_ext.cpp -o hello_ext.so -I /usr/lib -I /usr/include/boost -I /usr/include/python3.5m  -shared -fPIC -std=c++11 -lboost_python3  

