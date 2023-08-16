#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) > 0:
        for key, value in sorted(a_dictionary.items()):
            print("{}: {}".format(key, value))
    else:
        return
