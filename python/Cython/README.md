Cython
======

官网: http://cython.org/ 


1. simple example
--------------

把py转化成.so  

1. 编译python文件, 创建setup.py

    ```python
    from distutils.core import setup
    from Cython.Build import cythonize
    setup(
        ext_modules = cythonize("test.py")
    )
    ```

2. 然后运行
    python setup.py build_ext --inplace