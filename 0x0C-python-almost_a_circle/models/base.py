#!/usr/bin/python3
"""Module that contains Base class"""


class Base:
    """Base class for other subclasses"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of an object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
