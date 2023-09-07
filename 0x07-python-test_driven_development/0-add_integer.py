#!/usr/bin/python3
"""This module defines an integer addition function"""


def add_integer(a, b=98):
    """
    Returns an integer addition of a and b.

    Args:
        a (int | float): The first number.
        b (int | float): The second number. Defaults to 98 if not provided.

    Raises:
        TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
