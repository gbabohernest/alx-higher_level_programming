#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, col in enumerate(row):
            if (col == row[-1]):
                print("{:d}".format(col), end="")
            else:
                print("{:d}".format(col), end=" ")
        print()
