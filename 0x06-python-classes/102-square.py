#!/usr/bin/python3

"""
   Defines a square with a private
   instance attribute size = 0
"""


class Square:

    """create an instance with size=0"""
    def __init__(self, size=0):
        self.size = size

    """get the size"""
    @property
    def size(self):
        return self.__size

    """set the size"""
    @size.setter
    def size(self, value):
        if type(value) == int or type(value) == float:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be a number")

    """return the area of the square"""
    def area(self):
        return (self.__size * self.__size)

    """define == comparision of instances"""
    def __eq__(self, obj):
        return self.area() == obj.area()

    """define != comparision of instances"""
    def __ne__(self, obj):
        return self.area() != obj.area()

    """define < comparision of instances"""
    def __lt__(self, obj):
        return self.area() < obj.area()

    """define <= comparision of instances"""
    def __le__(self, obj):
        return self.area() <= obj.area()

    """define > comparision of instances"""
    def __gt__(self, obj):
        return self.area() > obj.area()

    """define >= comparision of instances"""
    def __ge__(self, obj):
        return self.area() >= obj.area()
