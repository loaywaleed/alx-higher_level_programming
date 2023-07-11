#!/usr/bin/python3
"""function that adds attributes"""


def add_attribute(obj, name, vame):
    """Add a new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
