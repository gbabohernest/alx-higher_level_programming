#!/usr/bin/python3
"""Defines a function that prints user fullname"""


def say_my_name(first_name, last_name=""):
    """Prints name.
    My name is <first name> <last name>

    args:
        fist_name - must be a string
        last_name - must be a string

    Raises:
        TypeError: first_name must be string
                   or last_name must be string.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
