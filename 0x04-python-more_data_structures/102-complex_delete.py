#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if a_dictionary is not None:
        keys_to_delete = []
        for key, v in a_dictionary.items():
            if v == value:
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del a_dictionary[key]

    return a_dictionary
