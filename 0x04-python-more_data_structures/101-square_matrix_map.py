#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda i: (list(map(lambda n: n * n, i))), matrix)))
