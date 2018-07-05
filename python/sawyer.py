import functools
import datetime


class LazyProperty(object):
    """ A property that caches itself to the class object. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter = func

    def __get__(self, obj, cls):
        value = self.getter(cls)
        setattr(cls, self.__name__, value)
        return value


class Properties:
    """ a class, aotu set properties. """

    is_sington = None
    is_update_attrs = None

    class Settings:
        author = "sawyer"
        attrs = {}

    class Sington:

        sing_class = None
        create_time = None

    def __new__(cls, *args, **kwargs):

        if cls.is_sington:
            if not cls.Sington.sing_class:
                cls.Sington.sing_class = super(Properties, cls).__new__(cls)
                cls.Sington.create_time = datetime.datetime.now()
            return cls.Sington.sing_class
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
        return self.__dict__.get(p , self.Settings.attrs.get(p, None))

    def set_properties(self, **kwargs):

        for p, v in kwargs.items():
            setattr(self, p, v)

    def properties(this, properties=None):

        if isinstance(properties, (list, tuple)):
            return [getattr(this, properties) for p in properties]

        if isinstance(properties, str):
            return getattr(this, properties)


class Test(Properties):
    is_update_attrs = True
    is_sington = True

t = Test(name="shihongguang")

t.name = 222

b = Test(name="shihongguang111")
print(b.name)
