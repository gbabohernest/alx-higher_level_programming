#!/usr/bin/python3
"""This module defines a function
   for writting a string to a text file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file(UTF8)"""
    with open(filename, mode="w", encoding="utf8") as file_obj:
        num_of_chars = file_obj.write(text)
    return num_of_chars
