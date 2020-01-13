#!/usr/bin/python3

"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """
    listError = 'matrix must be a matrix (list of lists) of integers/floats'
    sizeError = 'Each row of the matrix must have the same size'
    if type(matrix) is not list:
        raise TypeError(listError)
    for item in range(len(matrix)):
        if item is not 0:
            result = item - 1
            if len(matrix[item]) is not len(matrix[result]):
                raise TypeError(sizeError)
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in m_list] for m_list in matrix]
