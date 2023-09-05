#!/usr/bin/python3

""" A function that adds two integers """


def add_integer(a, b=98):
    """ Returns an integer addtion
        of a and b
    args:
         a (int | float)
         b (int | float)
    Raise:
         TypeError: a must be an integer
                    b must be an integer
    """

    if (not isinstance(a, float) and not isinstance(a, int)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, float) and not isinstance(b, int)):
        raise TypeError("b must be an integer")

    int_a = int(a)
    int_b = int(b)

    return int_a + int_b
