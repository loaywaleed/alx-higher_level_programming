#!/usr/bin/python3
"""instance inherited or not"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class that inherited
    from a specific class, otherwise false
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

