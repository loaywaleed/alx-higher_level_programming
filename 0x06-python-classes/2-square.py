#!/usr/bin/python3
""" Defines a class called Square """


class Square:
    """A square class
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square with private size
        Args:
            size (int): size of side in the square
        Returns: None
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
