#!/usr/bin/python3
"""Defines a Function that return
   a dictionary representation of
   simple data structure for JSON
   serialization of an object
"""


def class_to_json(obj):
    """Returns a dictionary
    description of a class
    """

    return (getattr(obj, "__dict__"))
