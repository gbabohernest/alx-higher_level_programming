#!/usr/bin/python3

"""
    safe_print_list: prints x elements of a list
    @my_list: a list of elements
    @x: num of element to print
    return: total num of elements printed
"""


def safe_print_list(my_list=[], x=0):

    num_of_ele_printed = 0
    try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            num_of_ele_printed += 1
    except IndexError as error:
        pass
    print()
    return num_of_ele_printed
