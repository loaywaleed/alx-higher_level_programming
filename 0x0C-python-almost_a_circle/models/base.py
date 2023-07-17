#!/usr/bin/python3
"""Module that contains Base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that converts objects to json strings"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that saves objs to file"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []
        if list_objs:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())

        json_str = cls.to_json_string(list_dic)
        with open(filename, 'w', encoding="utf-8") as my_file:
            my_file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Method that converts to objs from json"""
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """Method that creates an instance with specific attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that loads from a file"""
        filename = f"{cls.__name__}.json"
        try:
            my_list = []
            with open(filename) as my_file:
                dict_list = cls.from_json_string(my_file.read())
                for dic in dict_list:
                    my_list.append(cls.create(**dic))
                return my_list
        except IOError:
            return []
