#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """Args:
        obj: takes in an object
        return: a list of available attributes
    """
    return dir(obj)
