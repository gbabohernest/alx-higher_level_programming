#!/usr/bin/python3
"""This modules defines division matrix functions"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: list of lists of (int | float).
        div: must be a number (int | float) and can't be == 0

    Raises:
        TypeError: if matrix  is not a list of list of int | floats.
        TypeError: if each row of the matrix is not the same size
        ZeroDivisionError: if div == 0

    Return: a new matrix

    """
    new_matrix = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    size_err_msg = "Each row of the matrix must have the same size"

    try:
        length = len(matrix[0])
    except Exception:
        pass

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(err_msg)
        if length != len(row):
            raise TypeError(size_err_msg)
        for ele in row:
            if not isinstance(ele, (int, float)):
                raise TypeError(err_msg)
            result = round(ele / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
