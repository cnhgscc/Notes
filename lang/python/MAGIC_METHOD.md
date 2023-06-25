MAGIC METHOD
============

1. descriptor: 一般用于自定义class属性.
    1. 设置属性.由于描述器使用时可以得到类的实例,可以将要保存的内容直接保存到instance.__dict__中.也可以保存在描述器对象中, 即直接绑定在实例上.
    2. 获取属性.可以获取实例对象的类属性,对象属性,对象描述器中保存的内容.  


    ```python
    class Descriptor:
        """描述器使用时是把类的属性赋值为一个描述器对象

		类的对象在调用类的这个描述器属性时优先类描述器的行为, 是__setattr__, __getattr__ 方法中设定的

		行为: 如果设置对象的属性和类的属性同名
			1.如果类的这个属性不是描述器会把这个属性直接放到对象的__dict__中
			2.如果是描述器,按描述器的行为
		注意:
			1.如果使用类名给这个描述器类属性赋值时会把描述器换成新值,如果新值不是描述器,描述器的行为会消失
			2.如果是使用类名调用这个类属性时会调用描述器的方法, 其中instance参数会变为None


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

		def __setattr__(self, key, value):
			"""对象添加新属性或修改属性时调用该方法, 默认时该方法会优先使用同名类属性的描述器
			即当重新该方法时可以不让其使用描述器 
			"""
			
			# ----- test -----
			if key == "name":
				self.__dict__["name"] = value
			else:
				super().__setattr__(key, value)
			# ----------------

			pass
		
		def __getattr__(self, key):
			"""默认也是先调用同名类属性的描述器
			即 self.__dict__ 中有该属性, 也先描述器的行为
			"""

			pass

    ```
