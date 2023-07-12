#!/usr/bin/python3
"""Modules that has a function that appends string"""


def append_after(filename="", search_string="", new_string=""):
    """function that appends after a searched string"""
    text = ""
    with open(filename, encoding="utf-8") as my_file:
        for line in my_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as new_file:
        new_file.write(text)
