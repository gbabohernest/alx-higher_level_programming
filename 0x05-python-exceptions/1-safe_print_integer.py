#!/usr/bin/python3

"""
    safe_print_integer - prints an integer with {:d}.format()
    @value: can be any type(int, str, list etc)
    return: True if value is int, false otherwise
"""


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return (True)
        else:
            raise ValueError("only integer is alllowed")
    except ValueError:
        return (False)
