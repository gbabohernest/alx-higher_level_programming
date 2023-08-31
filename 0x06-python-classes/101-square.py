#!/usr/bin/python3

"""
   A class that defines a square instance
   with optional size and position attributes
"""


class Square:
    """create an a new instance with optional
       size and position attributes
       @size: arg (int)
       @position: arg (tuple)
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
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

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

    """return the area of the square"""
    def area(self):
        return (self.__size * self.__size)

    """print square instance with # char"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    """represent how the square should be printed"""
    def __str__(self):
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
