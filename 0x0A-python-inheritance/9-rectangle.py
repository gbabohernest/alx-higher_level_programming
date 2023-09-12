#!/usr/bin/python3
"""This module defines a Rectangle class
   that Inherits from BaseGeometry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Full Rectangle."""

    def __init__(self, width, height):
        """Instantiate with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""

        area = self.__width * self.__height
        return area

    def __str__(self):
        """Print an instance in a nice
           human readable format
        """
        s = "[{}] {}/{}".format(type(self).__name__,
                                self.__width, self.__height)
        return s
