#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for row in matrix:
        create_row = list(map(lambda col: col ** 2, row))
        new_list.append(create_row)
    return new_list
