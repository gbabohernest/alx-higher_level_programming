#!/usr/bin/python3

def search_replace(my_list, search, replace):

    if my_list is not None and search is not None and replace is not None:

        new_list = []
        for index, item in enumerate(my_list):
            if item == search:
                item = replace
            new_list.append(item)

        return new_list
