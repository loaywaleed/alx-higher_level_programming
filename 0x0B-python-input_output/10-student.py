#!/usr/bin/python3
"""module that has student class"""


class Student:
    """class that models a student"""
    def __init__(self, first_name, last_name, age):
        """instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict respresentation of a student"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for atr in attrs if hasattr(self, attr)}
