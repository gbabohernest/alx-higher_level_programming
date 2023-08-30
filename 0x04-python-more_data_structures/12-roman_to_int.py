#!/usr/bin/python3

"""
    converts a roman numberal
    to an integer
"""


def roman_to_int(roman_string):

    if (type(roman_string) is not str
       or roman_string is None):
        return (0)

    roman_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_num = 0

    for index in range(len(roman_string)):
        if roman_values.get(roman_string[index], 0) == 0:
            return (0)
        if (index != (len(roman_string) - 1) and
           roman_values[roman_string[index]] <
           roman_values[roman_string[index + 1]]):
            roman_num += roman_values[roman_string[index]] * -1
        else:
            roman_num += roman_values[roman_string[index]]

    return (roman_num)
