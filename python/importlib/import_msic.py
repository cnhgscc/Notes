from importlib import import_module


__all__ = ["import_module", "import_class"]

def import_class(model_class):
    _import_model_, _import_class_ = model_class.rsplit(".", 1)
    _import_model_ = import_module(_import_model_)

    try:
        _import_class_ = getattr(_import_model_, _import_class_)
    except AttributeError:
        raise ImportError(model_class)

    return _import_class_