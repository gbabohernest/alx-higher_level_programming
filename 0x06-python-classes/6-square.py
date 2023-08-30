#!/usr/bin/python3

"""
  Square: define a square instance
"""


class Square():
    """
        __init__: initialize a private instance attributes
        @size:  integer arg  Zero or greater than zero
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """
         area - calculate square area
         return: current sq area
    """
    def area(self):
        result = self.__size * self.__size
        return result

    """
        Retrieve private instance attribute
    """
    @property
    def size(self):
        return self.__size

    """
       set private instance attribute
    """
    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """
        Retrieve private instance attribute
    """
    @property
    def position(self):
        return self.__position

    """
        set private instance attribute
    """
    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        return TypeError("position must be a tuple of 2 positive integers")

    """
        prints to the stdout the square with the char '#'
        newline if size is zero
    """
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        char = "#"
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("{}".format(char), end="")
            print("")
