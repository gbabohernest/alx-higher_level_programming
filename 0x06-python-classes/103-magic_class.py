#!/usr/bin/python3

"""
    Define a class that does exactly
    as a python bytecode

    Representation of a circle
"""
import math


class MagicClass:
    """
        instantiate the magic class
        @radius : int or float
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """Return the area of the cirle"""
    def area(self):
        return (self.__radius ** 2 * math.pi)

    """return circumference of the circle"""
    def circumference(self):
        return (2 * math.pi * self.__radius)
