#!/usr/bin/python3
"""This module defines a function that checks
   if an instance is of a class that inherited
   (directly, indirectly) from a specified class.

   Return True, otherwise False
"""


def inherits_from(obj, a_class):
    """Return True if obj is from an
    inherited class, False otherwise
    """
    type_of_obj = type(obj)

    if (issubclass(type_of_obj, a_class) and type(obj) != a_class):
        return True
    return False
