#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    if my_list is not None:
        my_set = set(my_list)
        for i in my_set:
            result += i
    return result
