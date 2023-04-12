#!/usr/bin/python3
"""defines a JSON-object function"""


import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    return json.loads(my_str)
