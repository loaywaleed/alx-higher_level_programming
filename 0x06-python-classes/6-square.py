#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """A square class
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with private size
        Args:
            size (int): size of side in the square
        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(number, int) for number in value)
                or not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints a square
        Returns:
            None
        """
        if self.size == 0:
            print()
        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.size):
            for pos_x in range(0, self.position[0]):
                print(' ', end='')
            for j in range(0, self.size):
                print('#', end='')
            print("")
