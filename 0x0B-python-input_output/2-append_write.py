#!/usr/bin/python3
"""function that write to a file"""


def append_write(filename="", text=""):
    """function that appends to a file"""
    with open(filename, 'a', encoding="utf-8") as my_file:
        return my_file.write(text)
