#!/usr/bin/python3
"""
Module to find the max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """

    def test_max_integer(self):
        '''
        Test if integer is max integer
        '''
        result = max_integer([1, 4, 3, 2])
        self.assertEqual(result, 4)
        result = max_integer([12, 9, 7, 2])
        self.assertEqual(result, 12)

    def test_isint(self):
        '''
        Is it an integer?
        '''
        number = 24
        self.asserTrue(max_integer([number, 2]) == 2)


    if __name__ == '__main__':
        unittest.main()
