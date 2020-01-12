#!/usr/bin/python3

"""
Divides a matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix
    """
    if div is 0:
        raise ZeroDivisionError('division by zero')
    for item in range(len(matrix)):
        if item is not 0:
            result = item -1
            if len(matrix[item]) is not len(matrix[result]):
                raise TypeError('Each row of the matrix must have the same size')

    return [[round(item  / div,2) for item in matrix_list] for matrix_list in matrix]
