#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a_length = len(tuple_a)
    tuple_b_length = len(tuple_b)

    if tuple_a_length >= 2 and tuple_b_length >= 2:
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return result
    elif tuple_a_length == 1 and tuple_b_length == 1:
        result = (tuple_a[0] + tuple_b[0], 0 + 0)
        return result
    elif tuple_a_length >= 2 and tuple_b_length == 1:
        result = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        return result
    elif tuple_b_length >= 2 and tuple_a_length == 1:
        result = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
        return result
    elif tuple_a_length == 0 and tuple_b_length >= 2:
        result = (0 + tuple_b[0],  0 + tuple_b[1])
        return result
    elif tuple_a_length >= 2 and tuple_b_length == 0:
        result = (tuple_a[0] + 0, tuple_a[1] + 0)
        return result
    elif tuple_a_length == 1 and tuple_b_length == 0:
        result = (tuple_a[0] + 0, 0 + 0)
        return result
    elif tuple_a_length == 0 and tuple_b_length == 1:
        result = (0 + tuple_b[0], 0 + 0)
        return result
    return result (0, 0)
