#!/usr/bin/python3
"""This module defines a Rectangle Class
that inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate a rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set private instance attribute width."""
        self.validate_attributes("width", value)
        self.__width = value

    @property
    def height(self):
        """Get private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """set private instance attribute height."""
        self.validate_attributes("height", value)
        self.__height = value

    @property
    def x(self):
        """Get private instance attribute x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set private instance attribute x."""
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        """Get private instance attribute y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set private instance attribute y."""
        self.validate_attributes("y", value)
        self.__y = value

    def area(self):
        """Return the area of the rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle
        instance with the character #.
        """
        for _ in range(self.__height):
            for _ in range(self.__width):
                print('#', end="")
            print()

    @staticmethod
    def validate_attributes(attr, value):
        """Validates instance attribute."""
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")
        if attr == "width" or attr == "height":
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")

    def __str__(self):
        """Print the instance in human-readable format"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)
