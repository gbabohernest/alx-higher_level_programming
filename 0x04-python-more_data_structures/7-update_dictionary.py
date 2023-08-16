#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if  isinstance(key, str) and a_dictionary is not None:
        a_dictionary[key] = value
        return a_dictionary
    else:
        return
