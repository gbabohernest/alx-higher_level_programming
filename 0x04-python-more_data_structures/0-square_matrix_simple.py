#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if len(matrix) > 0:
        new_list = []
        for row in matrix:
            new_list.append(list(map(lambda x: x ** 2, row)))
        return new_list
    else:
        return []
