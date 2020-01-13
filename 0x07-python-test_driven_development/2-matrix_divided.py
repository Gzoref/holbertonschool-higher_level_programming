#!/usr/bin/python3

"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for item in range(len(matrix)):
        if item is not 0:
            result = item -1
            if len(matrix[item]) is not len(matrix[result]):
                raise TypeError('Each row of the matrix must have the same size')
    if isinstance(div, int) is False:
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item  / div,2) for item in matrix_list] for matrix_list in matrix]
