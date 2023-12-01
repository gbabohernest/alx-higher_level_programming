#!/usr/bin/python3
"""This module defines a function to find
   peak in list of unsorted integers
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        middle = (low + high) // 2

        if list_of_integers[middle] > list_of_integers[middle + 1]:
            high = middle
        else:
            low = middle + 1

    return list_of_integers[low]
