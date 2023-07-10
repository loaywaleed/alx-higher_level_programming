#!/usr/bin/python3
"""checks if an object is an instance of a specific class"""


def is_kind_of_class(obj, a_class):
    """return: true if an object is an instance of the class.
    false otherwise
    """
    return isinstance(obj, a_class)
