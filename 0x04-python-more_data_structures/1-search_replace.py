#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    result = list(map((lambda num: replace if num == search else num), my_list))
    new_list.append(result)
    return new_list
