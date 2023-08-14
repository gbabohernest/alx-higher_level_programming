#!/usr/bin/python3

def max_integer(my_list=[]):

    max_value = 0
    if len(my_list) < 1:
        return None
    else:
        for index, num in enumerate(my_list):
            if num > max_value:
                max_value = num
        return max_value
