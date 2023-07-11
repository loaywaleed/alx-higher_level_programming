#!/usr/bin/python3
"""base geometry class and childclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that models rectangle"""
    def __init__(self, width, height):
        """init instance of rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
