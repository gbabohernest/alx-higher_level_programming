#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """a representation of a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """Create an instance of Rectangle
           @width: width of the rectangle
           @height: height of the rectangle
        Raise:
              TypeError: if width or height is not an integer
              ValueError: if width or height is less than zero
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width attribute of an instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute of an instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height attribute of an instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute of an instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter
           if width or height = 0:
           p = 0
           p = 2 * (height + width)
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        p = 2 * (self.__height + self.__width)
        return p

    def __str__(self) -> str:
        """print the rectangle with # char"""
        if (self.__width == 0 or self.__height == 0):
            return ""

        for _ in range(self.__height):
            for _ in range(self.__width):
                rectangle = "#" * self.__width + "\n"
                rectangle *= self.__height - 1
                rectangle += "#" * self.__width
        return rectangle

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message when an instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
