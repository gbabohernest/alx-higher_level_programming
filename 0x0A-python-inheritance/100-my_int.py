#!/usr/bin/python3
"""Defines a class that inherits from int
   built-in class.
"""


class MyInt(int):
    """A class the inherits form int."""

    def __init__(self, value):
        """Instantiate with the int
           class constructor
        """
        super().__init__()

    def __ne__(self, other):
        """Override the not equal operator (!=)."""
        result = super().__ne__(other)
        return not result

    def __eq__(self, other):
        """Override the equal operator (==)."""
        result = super().__eq__(other)
        return not result
