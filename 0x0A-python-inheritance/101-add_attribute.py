#!/usr/bin/python3
"""Defines a function that adds attribute"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an
       object if it's possible.

    Raises:
         TypeError: can't add new attribute
    """
    if '__dict__' in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
