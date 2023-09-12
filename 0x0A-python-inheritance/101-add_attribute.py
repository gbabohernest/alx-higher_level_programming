#!/usr/bin/python3
"""Defines a function that adds attribute"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an
       object if it's possible.

    Raises:
         TypeError: can't add new attribute
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")

    if not hasattr(obj, name):
        obj.__setattr__(name, value)
