#!/usr/bin/python3
"""
Unittest for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def empty_list_test(self):
        self.assertEqual(max_integer([]), None)

    def test_max_front(self):
        my_list = [5, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 5)

    def test_max_middle(self):
        my_list = [5, 2, 99, 3, 4]
        self.assertEqual(max_integer(my_list), 99)

    def test_max_end(self):
        my_list = [1, 2, 3, 4, 56]
        self.assertEqual(max_integer(my_list), 56)

    def test_max_long(self):
        my_list = [1, 2, 3, 4, 5, 77, 88, 99, 0, 56]
        self.assertEqual(max_integer(my_list), 99)

    def test_negative(self):
        my_list = [-1, -22, -3, -4]
        self.assertEqual(max_integer(my_list), -1)

    def mixed_cases_test(self):
        my_list = [2, 3, 4, 5, 'd']
        self.assertEqual(max_integer(my_list), "d")

    def isnone_test(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def with_string(self):
        self.assertEqual(max_integer("string"), "t")
