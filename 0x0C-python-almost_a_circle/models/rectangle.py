#!/usr/bin/python3
"""This module defines a Rectangle Class
   that inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle Class.
       Inherits from Base.
       Method:
            __init__()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate a rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    def update(self, *args, **kwargs):
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
        attr_names = ["id", "width", "height", "x", "y"]
        idx_to_attr = {0: 'id', 1: 'width', 2: 'height', 3: 'x', 4: 'y'}

        if args and len(args) != 0:

            for idx, arg in enumerate(args):
                if idx in idx_to_attr:
                    setattr(self, idx_to_attr[idx], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attr_names:
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

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "x": getattr(self, "x"),
            "y": getattr(self, "y"),
            "id": getattr(self, "id"),
            "height": getattr(self, "height"),
            "width": getattr(self, "width"),
        }
