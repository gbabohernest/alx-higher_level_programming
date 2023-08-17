#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is not None:
        biggest_key = None
        biggest_value = 0

        for key, value in a_dictionary.items():
            if isinstance(value, int):
                if value > biggest_value:
                    biggest_value = value
                    biggest_key = key

        return biggest_key

    else:
        return None
