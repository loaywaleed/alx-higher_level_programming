#!/usr/bin/python3
"""BaseGeometry class and subclass Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass that models a square"""
    def __init__(self, size):
        """int square object"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size * self.__size

    def __str__(self):
        """string of square"""
        return "[Square], {:d}/{:d}".format(self.__size, self.__size)
