#!/usr/bin/python3

def uniq_add(my_list=[]):

    if my_list is not None:
        uniq_value = set()
        result = 0

        for indx, value in enumerate(my_list):
            uniq_value.add(value)

        for i in uniq_value:
            result += i

        return result
