#!/usr/bin/python3
"""MyInt class module"""



class MyInt(int):
    """rebel version of an integer"""
    def __new__(cls, *args, **kwargs):
        """init instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= is now =="""
        return int(self) != other

    def __ne__(self, other):
        """== is now !="""
        return int(self) == other
