#!/usr/bin/python3

def no_c(my_string):
    if my_string is not None:
        new_str = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                new_str += char
        return new_str
