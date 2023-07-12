#!/usr/bin/python3
"""module that creates an object from a json file"""

import json


def load_from_json_file(filename):
    """function that loads object from a json file"""
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)
