#!/usr/bin/python3
"""A module that defines a function the checks
if an object is an instance of a class.
Return True, otherwise False
"""


def is_same_class(obj, a_class):
    """Return True if obj is an instance
       of a_class, otherwise false
    """
    if type(obj) is a_class:
        return True
    return False
