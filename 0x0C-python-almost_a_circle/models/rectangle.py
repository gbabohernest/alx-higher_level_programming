#!/usr/bin/python3
"""This module defines a Rectangle Class
that inherits from the Base class
"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the private instance
        attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the private instance
        attribute width"""
        self.__width = value

    @property
    def height(self):
        """Get private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set private instance attribute height"""
        self.__height = value

    @property
    def x(self):
        """Get private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set private instance attribute x"""
        self.__x = value

    @property
    def y(self):
        """Get private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set private instance attribute y"""
        self.__y = value
