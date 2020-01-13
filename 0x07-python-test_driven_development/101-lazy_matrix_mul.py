#!/usr/bin/python3

'''
Multiplies 2 matrices by using the module NumPy
'''

import numpy as np
def lazy_matrix_mul(m_a, m_b):
    '''
    Function multiplies two matrices with numpy
    '''
    if isinstance(m_a, list) is False:
        raise TypeError('m_a must be a list')
    if isinstance(m_b, list) is False:
        raise TypeError('m_b must be a list')
    if not (isinstance(item, list) for item in m_a):
        raise TypeError('m_a must be a list of lists')
    if not (isinstance(item, list) for item in m_b):
        raise TypeError('m_b must be a list of lists')
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(i, float) or isinstance(i, int)
            for l in m_a for i in l):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(i, float) or isinstance(i, int)
               for l in m_b for i in l):
        raise TypeError('m_b should contain only integers or floats')
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError('each row of m_a must should be of the same size')
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    a = np.array(m_a)
    b = np.array(m_b)
    c = np.dot(a, b)
    return c
