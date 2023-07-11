#!/usr/bin/python3
"""Integer validator class module"""


class BaseGeometry():
    """Class with area method and integer validator method"""
    def area(self):
        """returns that function is not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
