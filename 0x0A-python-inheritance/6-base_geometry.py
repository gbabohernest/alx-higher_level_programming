#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """A BaseGeometry class."""
    def __init__(self):
        """Instantiate an empty object"""
        pass

    def area(self):
        """
        This method raises an
        Exception when it is called
        """
        raise Exception("area() is not implemented")
