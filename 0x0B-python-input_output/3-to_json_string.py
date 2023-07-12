#!/usr/bin/python3
"""module that has a function that converts json to string"""

import json


def to_json_string(my_obj):
    """function that converts object to json string"""
    return json.dumps(my_obj)
