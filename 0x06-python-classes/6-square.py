#!/usr/bin/python3

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
        return self.__size

    """set the size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """get the position"""
    @property
    def position(self):
        return self.__position

    """set the position"""
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([num for idx, num in enumerate(value) if (lambda x:
                isinstance(x, int) and x >= 0)(num)]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """return the square area"""
    def area(self):
        return self.__size * self.__size

    """formats how spaces should
       be used when printing
    """
    def format_print(self):
        sp = ""
        if self.size == 0:
            return "\n"

        for _ in range(self.position[1]):
            sp += "\n"

        for _ in range(self.size):
            sp += " " * self.position[0] + "#" * self.size + "\n"
        return sp

    """prints in stdout the square with char #"""
    def my_print(self):
        print(self.format_print(), end='')

    def __str__(self):
        self.my_print()
