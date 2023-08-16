#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    if all([a_dictionary, key, value]) and isinstance(key, str):
        a_dictionary[key] = value
        return a_dictionary
    else:
        return
