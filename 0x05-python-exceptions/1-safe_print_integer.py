#!/usr/bin/python3

"""
    safe_print_integer - prints an integer with {:d}.format()
    @value: can be any type(int, str, list etc)
    return: True if value is int, false otherwise

"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
