#!/usr/bin/python4

"""
    Square: A class that define
    a square instance
"""


class Square():
    """
       create an instance with
       optional size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """get the size"""
    @property
    def size(self):
        return self.__size

    """set the size"""
    @size.setter
    def size(self, value):
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """get the position"""
    @property
    def position(self):
        return self.__position

    """set the position"""
    @position.setter
    def position(self, value):
        is_tuple = isinstance(value, tuple)
        is_len = len(value) == 2
        is_value_int = isinstance(value[0], int) and isinstance(value[1], int)
        is_positive_int = value[0] >= 0 and value[1] >= 0

        if all((is_tuple, is_len, is_value_int, is_positive_int)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """return the square area"""
    def area(self):
        return self.__size * self.__size

    """prints in stdout the square with char #"""
    def my_print(self):
        sp = ' '
        ch = '#'

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print("{}".format(sp * self.__position[0]), end='')
                print("{}".format(ch * self.__size))
