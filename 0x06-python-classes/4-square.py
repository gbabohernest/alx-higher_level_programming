#!/usr/bin/python3

"""
    A class that defines a square
    instance with an intial value
"""


class Square:
    """
        instantiate with an optional
        private attribute (size)

        @size: must be of type integer && >= 0
    """
    def __init__(self, size=0):
        self.__size = size

    """
        @property size -  will retrieve
        the private size attribute of an
        instance
    """
    @property
    def size(self):
        return self.__size

    """
        @property size setter - will set the value
        of the private size attribute after doing
        some checks

        @value : arg must of type int && > 0
    """
    @size.setter
    def size(self, value):
        is_int = isinstance(value, int)
        if not is_int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
        area - calculate the area of a square
        return: the area of a square
    """
    def area(self):
        return self.__size * self.__size
