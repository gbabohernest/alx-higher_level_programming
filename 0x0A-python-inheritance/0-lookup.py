#!/usr/bin/python3
"""A module that defines a function
that return a list of attributes and
methods of an object
"""


def lookup(obj):
    """Return a list object"""
    return dir(obj)
