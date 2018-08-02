MAGIC METHOD
============

1. descriptor: 一般用于自定义class属性.
    1. 设置属性.由于描述器使用时可以得到类的实例,可以将要保存的内容直接保存到instance.__dict__中.也可以保存在描述器对象中, 即直接绑定在实例上.
    2. 获取属性.可以获取实例对象的类属性,对象属性,对象描述器中保存的内容.

    ```python
    class Descriptor:
        """
        Parameters
        ----------
        owner: 描述器所描述的<类>, 选用
        instance: 描述器所描述的<类> 的 <实例>, 选用
        """
        def __init__(self, verbose_name):
            """设置描述器保存的内容

            例如: 描述器所描述的<类>中对象属性的说明, 属性保存的内容...
            """

            # ----- test -----
            self.verbose_name = verbose_name
            # ----------------

            pass

        def __get__(self, instance, owner):
            pass

        def __set__(self, instance, value):
            pass

        def __delete__(self, instance):
            pass

    # simple example
    class Person:

        name = Descriptor(verbose_name="person name")
    ```
