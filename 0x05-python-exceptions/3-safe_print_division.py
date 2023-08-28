#!/usr/bin/python3

"""
    safe_print_division - Divides 2 integers and prints the result
    @a: arg one
    @b: arg two
    return: value of division, otherwise None
"""


def safe_print_division(a, b):

    sum = 0
    try:
        if isinstance(a, int) and isinstance(b, int):
            if b == 0:
                raise ZeroDivisionError("division by zero not possible")
            sum = a / b
    except (ZeroDivisionError, TypeError, NameError) as error:
        sum = None
    finally:
        print("Inside result: {}".format(sum))
        return sum
