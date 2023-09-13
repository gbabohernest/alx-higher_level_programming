#!/usr/bin/python3
"""This module defines a function for inserting
   a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):

    """Appends a string after finding a keyword"""

    with open(filename, 'r', encoding="utf8") as fd:
        lines = fd.readlines()

    with open(filename, 'w', encoding="utf8") as fd:
        for line in lines:
            fd.write(line)
            if search_string in line:
                fd.write(new_string)
