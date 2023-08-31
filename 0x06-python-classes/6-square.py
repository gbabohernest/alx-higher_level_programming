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
        if (isinstance(value, tuple) and len(value) == 2 and
           all(isinstance(val, int) for val in value) and
           all(val >= 0 for val in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """return the square area"""
    def area(self):
        return self.__size * self.__size

    """prints in stdout the square with char #"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
