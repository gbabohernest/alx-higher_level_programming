#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and print
       its content to the stdout

       Agrs:
          filename: name of the file to be read
    """
    with open(filename, encoding="utf-8") as file_object:
        print(file_object.read(), end="")
