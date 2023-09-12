#!/usr/bin/python3
"""Defines a function for creating
   Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """Creates an Object from JSON file"""
    with open(filename, encoding="utf8") as file_object:
        py_obj = json.load(file_object)
    return py_obj
