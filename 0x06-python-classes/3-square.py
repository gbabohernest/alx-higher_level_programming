#!/usr/bin/python3

"""
    Defines a square instance
    with optional intial value
"""


class Square:
    """
        instantiate with an optional
        private attribute (size)

        @size: must be of type int && >= 0
    """
    def __init__(self, size=0):

        is_int = isinstance(size, int)
        if not is_int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    """
        area -  calculate the area of a square
        return: the area of a square
    """
    def area(self):
        return self.__size * self.__size
