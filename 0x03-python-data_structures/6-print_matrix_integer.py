#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix is not None:

        for row in matrix:
            for indx, col in enumerate(row):
                print("{:d}".format(col), end="")
            print()
