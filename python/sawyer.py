import functools
import datetime


class LazyClassProperty(object):
    """ A class property that caches itself to the class. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter = func

    def __get__(self, obj, cls):
        value = self.getter(cls)
        setattr(cls, self.__name__, value)
        return value


class LazyProperty(object):
    """ A instance property that caches itself to the class object. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter = func

    def __get__(self, obj, cls):
        value = self.getter(obj)
        setattr(obj, self.__name__, value)
        return value


class Properties:
    """ a class, auto set properties. """

    class Settings:
        author = "sawyer"
        default_attrs = {}

        is_sington = False
        is_update_attrs = True


    class SingtonProxy:

        sing_class = None
        create_time = None

    def __new__(cls, *args, **kwargs):

        for cls_p, cls_v in cls.Settings.__dict__.items():
            if not hasattr(cls, cls_p):
                setattr(cls, cls_p, cls_v)
        else:
            if not hasattr(cls, "default_attr"):
                cls.default_attr = {}
            if not hasattr(cls, "is_sington"):
                cls.is_sington = False
            if not hasattr(cls, "is_update_attrs"):
                cls.is_update_attrs = True

        if cls.is_sington:
            if not cls.SingtonProxy.sing_class:
                cls.SingtonProxy.sing_class = super(Properties, cls).__new__(cls)
                cls.SingtonProxy.create_time = datetime.datetime.now()
            return cls.SingtonProxy.sing_class
        else:
            return super(Properties, cls).__new__(cls)


    def __init__(self, **kwargs):
        self.set_properties(**kwargs)

    def __setattr__(self, p, v):
        if self.__class__.is_update_attrs:
            self.__dict__.update({p: v})
        else:
            self.__dict__.setdefault(p, v)

    def __getattr__(self, p):
        return self.__dict__.get(p, self.default_attrs.get(p, None))

    def set_properties(self, **kwargs):

        for p, v in kwargs.items():
            setattr(self, p, v)

    def properties(self, properties=None):

        if isinstance(properties, (list, tuple)):
            return [getattr(self, p) for p in properties]

        if isinstance(properties, str):
            return getattr(self, properties)


if __name__ == "__main__":

    class Test(Properties):

        class Settings:
            is_sington = True
            is_update_attrs = False

        @LazyProperty
        def age(self):
            return 20 + 7


    t1 = Test(name="shihongguang")
    t2 = Test(name="shihongguang1013")

    print(t1.name)
    print(t1.age)
    print(t1.__class__.__dict__)
    print(t1.__dict__)
