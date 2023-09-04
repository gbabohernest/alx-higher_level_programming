#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """a representation of a rectangle"""

    def __init__(self, width=0, height=0):

        """Create an instance of Rectangle
           @width: width of the rectangle
           @height: height of the rectangle
        Raise:
              TypeError: if width or height is not an integer
              ValueError: if width or height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width attribute of an instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute of an instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height attribute of an instance"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter
           if width or height = 0
           perimeter = 0
           p = 2 * (height + width)
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        p = 2 * (self.__height + self.__width)
        return p
