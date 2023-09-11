#!/usr/bin/python3
"""This module defines a
   class that inherits from list
"""


class MyList(list):
    """A class that inherits from List"""

    def __init__(self):
        """Instantiate a list object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending sort"""
        sorted_list = sorted(self)
        print(sorted_list)
