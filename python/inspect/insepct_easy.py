import instpect

def iprintmethod(iobj):

    properties = []
    method = []

    for m in inspect.getmembers(response):
        try:
            method.append("def {0}{1}:\n\t\"\"\"{2}\"\"\"".format(m[0], inspect.signature(m[1]), m[1].__doc__))
        except TypeError:
            properties.append(m)
        except (ValueError):
            pass

    list(map(print, properties))
    list(map(print, method))