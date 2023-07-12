#!/usr/bin/python3
"""module that has class_to_json function"""


def class_to_json(obj):
    """function that returns object for json serialization of an object"""
    return obj.__dict__
