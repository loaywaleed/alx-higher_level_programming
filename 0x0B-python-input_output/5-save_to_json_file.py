#!/usr/bin/python3
"""module that writes object to json file"""

import json


def save_to_json_file(my_obj, filename):
    """function that saves object to json file"""
    with open(filename, 'w', encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
