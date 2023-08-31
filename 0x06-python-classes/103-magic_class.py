#!/usr/bin/python3

"""
    Define a class that does exactly
    as a python bytecode

    Representation of a circle
"""


class MagicClass:
    """
        instantiate the magic class
        @radius : int or float
    """
    def __init__(self, radius=0):
        if type(radius) == int or type(radius) == float:
            self.__radius = radius
        else:
            raise TypeError("radius must a number")

    """Return the area of the cirle"""
    def area(self):
        return (self.__radius ** 2 * math.pi)

    """return circumference of the circle"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
