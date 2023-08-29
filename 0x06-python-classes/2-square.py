#!/usr/bin/python3

"""
    A class that defines a
    square instance with
    optional intial value
"""


class Square:
    """
        initialize an instance with optional
        privite attribute (size)

        @size: arg must be an integer && size > 0
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
