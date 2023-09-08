#!/usr/bin/python3
"""Defines a function that prints square"""


def print_square(size):
    """Prints a '#' character size times."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    char = '#'
    for item in range(size):
        print("{}".format(char * size), end="")
        print()
