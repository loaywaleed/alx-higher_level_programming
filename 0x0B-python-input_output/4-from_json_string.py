#!/usr/bin/python3
"""module that has a function that converts json to python object"""

import json


def from_json_string(my_str):
    """function that converts json to object"""
    return json.loads(my_str)

