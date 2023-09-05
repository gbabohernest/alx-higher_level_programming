#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize an instance of a Rectangle
           with optional width andd height attribute
           @width: width of the rectangle
           @height: height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of an instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of an instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height of an instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of an instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")

        self.__height = value
