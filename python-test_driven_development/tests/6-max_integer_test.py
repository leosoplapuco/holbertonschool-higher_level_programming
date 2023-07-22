#!/usr/bin/python3
"""module TestMaxInteger"""


import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.1, 4.9]), 4.9)

    def test_string_list(self):
        with self.assertRaises(TypeError):
            max_integer(["1", "2", "3"])


if __name__ == '__main__':
    unittest.main()
