#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_value = [0, 0]
    b_value = [0, 0]

    for index, item in enumerate(tuple_a):
        if index < 2:
            a_value[index] = tuple_a[index]

    for index, item in enumerate(tuple_b):
        if index < 2:
            b_value[index] = tuple_b[index]

    result = [a_value[0] + b_value[0], a_value[1] + b_value[1]]
    return tuple(result)
