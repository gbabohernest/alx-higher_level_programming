#!/usr/bin/python3
"""A module that defines a function that checks
   if an object is an instance, or an instance
   of a class that inherited from a specified class.

   Return True, otherwise False
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance
    of a_class, False otherwise
    """
    return isinstance(obj, a_class)
