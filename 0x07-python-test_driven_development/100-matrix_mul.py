#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two(2) matrices.

    args:
        m_a - a list of lists of integers | floats.
        m_b - a list of lists of integers | floats.

    Raises:
        TypeError: if m_a or m_b is not a list.
                   if m_a or m_b is not a list of lists.
                   if one element of m_a or m_b is not int | float.
                   if m_a or m_b is not a rectangle, all rows should
                   be of the same size.

        ValueError: if m_a or m_b is empty.
                    if m_a and m_b can't be mutiplied.

    """
    new_matrix = []
    # check if matrices are valid
    matrices_handler(m_a, m_b)

    for row_a in m_a:
        tmp_row = []
        for col_b in zip(*m_b):  # Transpose m_b for easier multiplication
            # Calculate the inner product of row_a and col_b
            inner_product = sum(a * b for a, b in zip(row_a, col_b))
            tmp_row.append(inner_product)
        new_matrix.append(tmp_row)

    return new_matrix


def matrices_handler(m_a, m_b):
    """Validate matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
