#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) > 0:
        sorted_dic = {}
        for key, value in sorted(a_dictionary.items()):
            sorted_dic[key] = value

        return sorted_dic
    else:
        return {}
