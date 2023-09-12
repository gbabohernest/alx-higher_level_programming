#!/usr/bin/python3
"""Defines a function that
   return the JSON representation
   of an object
"""

import json


def to_json_string(my_obj):
    """Return a JSON string"""
    result = json.dumps(my_obj)
    return result
