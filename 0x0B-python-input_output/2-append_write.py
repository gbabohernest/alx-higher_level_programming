#!/usr/bin/python3
"""Defines a function for appending
   a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, mode="a", encoding="utf8") as file_obj:
        num_of_char = file_obj.write(text)
    return num_of_char
