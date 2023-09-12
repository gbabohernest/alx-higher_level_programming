#!/usr/bin/python3
"""Defines a function for deserializing
   a JSON string to a Python's object
"""


import json


def from_json_string(my_str):
    """Return a Python's object
       from JSON string
    """
    py_obj = json.loads(my_str)
    return py_obj
