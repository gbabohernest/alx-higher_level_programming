#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if my_list is not None and len(my_list) > 0:

        new_list = []
        for item in my_list:
            if item % 2 == 0:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
