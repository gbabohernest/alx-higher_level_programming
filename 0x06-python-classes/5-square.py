#!/usr/bin/python3

"""
  Square: define a square instance
          with an initial value
"""


class Square:
    """
        __init__: create an instance optional
                  private attribute (size)
         @size: integer args && >= 0
    """
    def __init__(self, size=0):
        self.__size = size

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
        area - calculate square area
        return: result
    """
    def area(self):
        result = self.__size * self.__size
        return result

    """
        prints to the stdout the  square with the char '#'
        newline if size is zero
    """
    def my_print(self):
        if self.__size == 0:
            print()
            return
        char = "#"
        for i in range(self.__size):
            for j in range(self.__size):
                print("{}".format(char), end="")
            print()
