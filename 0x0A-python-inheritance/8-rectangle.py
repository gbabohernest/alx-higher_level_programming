#!/usr/bin/python3
"""This module defines a Rectangle class
   the Inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a Rectangle."""
    def __init__(self, width, height):
        """Instantiate with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
