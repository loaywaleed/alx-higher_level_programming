#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """A square class
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square with private size
        Args:
            size (int): size of side in the square
        Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """Gets the value of size
        Returns:
            The size of square side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of side size
        Args:
            value (int): The size of square side
        Returns:
            None
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Finds area of square
        Returns:
            Area of the square
        """
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Prints a square
        Returns:
            None
        """
        if self.size == 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()
