import sys
import os

from importlib import import_module


__all__ = ["import_module", "import_class"]

def import_class(model_class:str):

    _import_model_, _import_class_ = model_class.rsplit(".", 1)
    _import_model_ = import_module(_import_model_)

    try:
        _import_class_ = getattr(_import_model_, _import_class_)
    except AttributeError:
        raise ImportError(model_class)

    return _import_class_


def import_file(filepath):
    abspath = os.path.abspath(filepath)
    dirname, file = os.path.split(abspath)
    fname, fext = os.path.splitext(file)

    if fext != '.py':
        raise ValueError("Not a Python source file: %s" % abspath)
    if dirname:
        sys.path = [dirname] + sys.path
    try:
        module = import_module(fname)
    finally:
        if dirname:
            sys.path.pop(0)
    return module
