#!/usr/bin/python3
"""
   Defines a locked class with
   no class or object attribute
"""


class LockedClass:
    """
    Prevents the user from instantiating new attributes
    other than attributes call 'first_name'.
    """
    __slots__ = ["first_name"]
