#!/usr/bin/python3

'''
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''
    Create a function def pascal_triangle(n):
    that returns a list of lists of integers
    representing the Pascal’s triangle of n
    '''
    triangle = []
    for position in range(1, n + 1):
        triangle.append([1] * position)
    for y in range(2, n):
        row = triangle[y]
        prev_row = triangle[y - 1]
        for x in range(1, len(row) - 1):
            row[x] = prev_row[x - 1] + prev_row[x]
    return triangle
