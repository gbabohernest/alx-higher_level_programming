#!/usr/bin/python3
"""This module defines a function for
   creating pascal triangle
"""


def pascal_triangle(n):
    """Creates a pascal triangle
    Return: A matrix containing
            integers representing
            the pascal triangle of n
    """

    matrix = []

    for row in range(n):
        row_values = []
        for col in range(row + 1):
            if col == 0 or col == row:
                row_values.append(1)
            else:
                prev_row = matrix[row - 1]
                value = prev_row[col] + prev_row[col - 1]
                row_values.append(value)
        matrix.append(row_values)

    return matrix
