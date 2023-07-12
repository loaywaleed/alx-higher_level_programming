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
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """replaces attributes of the student instance"""
        for el in json:
            try:
                setattr(self, el, json[el])
            except FileNotFoundError:
                pass
