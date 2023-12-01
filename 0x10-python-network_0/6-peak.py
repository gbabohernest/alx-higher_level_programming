#!/usr/bin/python3
"""This module defines a function to find
   peak in list of unsorted integers 
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if list_of_integers is None or not list_of_integers:
        return None

    for number in range(1, len(list_of_integers) - 1):
        neighbor_1 = list_of_integers[number - 1]
        neighbor_2 = list_of_integers[number + 1]

        if list_of_integers[number] >= neighbor_1 and list_of_integers[number] >= neighbor_2:
            return list_of_integers[number]

    return None
