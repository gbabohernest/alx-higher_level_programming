#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    if isinstance(key, str) and a_dictionary is not None:
        if key in a_dictionary:
            del (a_dictionary[key])
            return a_dictionary
        else:
            return a_dictionary
