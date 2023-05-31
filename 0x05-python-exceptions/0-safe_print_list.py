#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    num_of_elements = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]),end="")
            num_of_elements += 1
    except IndexError:
        pass
    print()
    return (num_of_elements)
