#!/usr/bin/python3
"""This modules defines a class Square
   that inherits from Rectangle class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Defines a Square."""
    def __init__(self, size):
        """Instantiate with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        area = self.__size * self.__size
        return area
