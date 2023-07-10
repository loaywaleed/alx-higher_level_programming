#!/usr/bin/python3
"""MyList Class that inherits from list"""


class MyList(list):
    """childclass of list"""
    def __init__(self):
        """Inits instance"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
