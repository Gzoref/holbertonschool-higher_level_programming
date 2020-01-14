#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def variable_test(self):
        a = 77
        self.assertEqual(max_integer([a]), a)

    def test_max_front(self):
        my_list = [5, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 5)

    def test_max_middle(self):
        my_list = [5, 2, 99, 3, 4]
        self.assertEqual(max_integer(my_list), 99)

    def test_end(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_negative(self):
        my_list = [1, -22, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def empty_list_test(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def mixed_cases_test(self):
        my_list = [2, 3, 4, 5, 'd']
        self.assertRaises(TypeError, max_integer, my_list)
