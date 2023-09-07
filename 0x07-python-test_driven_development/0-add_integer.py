#!/usr/bin/python3

"""Defines an integer addition function"""


def add_integer(a, b=98):
    """ Returns an integer addtion
        of a and b
    args:
         a (int | float)
         b (int | float)
    Float arguments are tpycasted to integer before addition
    Raise:
         TypeError: a must be an integer
                    b must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    int_a = int(a)
    int_b = int(b)

    return int_a + int_b
