#!/usr/bin/python3

"""
    safe_print_list_integers - prints the first x elemets
                               of a list and only integers
    @my_list: a list of elements
    @x: num of elements to access
    return: total num of elements printed
"""


def safe_print_list_integers(my_list=[], x=0):
    num_of_elem_printed = 0
    try:
        for item in range(0, x):
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end="")
                num_of_elem_printed += 1
            else:
                continue
    except (TypeError, ValueError):
        pass
    print()
    return num_of_elem_printed
