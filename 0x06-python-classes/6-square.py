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
        self.size = size
        self.position = position

    """get the size"""
    @property
    def size(self):
        return (self.__size)

    """set the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """get the position"""
    @property
    def position(self):
        return (self.__position)

    """set the position"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """return the square area"""
    def area(self):
        return (self.__size * self.__size)

    """prints in stdout the square with char #"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
