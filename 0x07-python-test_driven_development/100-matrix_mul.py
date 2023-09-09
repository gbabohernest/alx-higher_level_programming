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

    for a_list in m_a:
        tmp_list = [0] * (len(a_list))
        for idx, n in enumerate(a_list):
            try:
                for idp, p in enumerate(m_b[idx]):
                    tmp_list[idp] += n * p
            except Exception:
                raise ValueError("m_a and m_b can't be multiplied")
        new_matrix.append(tmp_list)
    return new_matrix


def matrices_handler(m_a, m_b):
    """Validate matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
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
