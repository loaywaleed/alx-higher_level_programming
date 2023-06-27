#!/usr/bin/python3
""" Defines a class called Square
"""

class Square():
    """ A square class
    Attributes:
        __size: size of a side of the square
    """
    def __init__(self, size):
        """ Initializes a square with private size
        Args:
            size: size of side in the square
        Returns: None
        """
        self.__size = size
