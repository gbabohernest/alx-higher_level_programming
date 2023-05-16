#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    
    for row in matrix:
        for idx, item in enumerate(row):
            print("{:d}".format(item), end=" ")
        print()
