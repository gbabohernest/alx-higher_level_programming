#!/usr/bin/python3
"""This module defines a function
   for writing an object to a text
   file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a textfile
       using JSON representation
    """

    with open(filename, "w", encoding="utf8") as file_object:
        json.dump(my_obj, file_object)
