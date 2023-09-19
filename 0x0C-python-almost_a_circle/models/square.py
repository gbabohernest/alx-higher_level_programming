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

    def __str__(self):
        """Print the instance in human-readable format"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
