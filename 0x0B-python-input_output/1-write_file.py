#!/usr/bin/python3
"""module that has write_file function"""


def write_file(filename="", text=""):
    """function that writes to a file"""
    with open(filename, mode='w', encoding="utf-8") as my_file:
        return my_file.write(text)
