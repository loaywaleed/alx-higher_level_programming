#!/usr/bin/python3
"""Module that contains rectangle childclass"""

from models.base import Base


class Rectangle(Base):
    """Rectangle childclass that inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
