#!/usr/bin/python3
"""This module defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class inherits from Rectangle, Base."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate a new square.
        Args:
            size: size of the square (int)
            x: coordinate x (int)
            y: coordinate y (int)
            id: square identity (int)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the width of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set width & height of the square"""
        self.validate_attributes("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Print the instance in human-readable format"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
               Args:
                   *args - a tuple of integers to be assigned
                           as new attribute value
                   **kwargs - assigns key/value argument to attribute
        1 -> id attribute
        2 -> width attribute
        3 -> height attribute
        4 -> x attribute
        5 -> y attribute
        """
        attr_names = ["id", "size", "x", "y"]
        idx_to_attr = {0: 'id', 1: 'size', 2: 'x', 3: 'y'}

        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                if idx in idx_to_attr:
                    setattr(self, idx_to_attr[idx], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)
