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
        rect = ""
        print("\n" * self.y, end="")
        for _ in range(self.__height):
            rect += (" " * self.x) + ("#" * self.__width) + "\n"
        print(rect, end="")

    def update(self, *args):
        """Assigns an argument to each attribute
        Args:
            *args - a tuple of integers to be assigned as new attribute value
            **kwargs - assigns key/value argument to attribute

        1 -> id attribute
        2 -> width attribute
        3 -> height attribute
        4 -> x attribute
        5 -> y attribute
        """
        if args and len(args) != 0:
            attr_names = ["id", "width", "height", "x", "y"]
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.width = arg
                elif idx == 2:
                    self.height = arg
                elif idx == 3:
                    self.x = arg
                elif idx == 4:
                    self.y = arg

                # setattr(self, attr_names[idx], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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
