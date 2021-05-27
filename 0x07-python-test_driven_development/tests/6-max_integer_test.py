#!/usr/bin/python3
"""
Unittests for 6-max_integer.py
"""

import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for unittests for max_integer """
    def test_pos(self):
        """ Test positive integers """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_neg(self):
        """ Test negative integers """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_dup(self):
        """ Test with duplicated values """
        self.assertEqual(max_integer([-11, 36, -3, -11, 36, 34]), 36)

    def test_float(self):
        """ Test floats """
        self.assertEqual(max_integer([-1, 2.3, 4.5, -4.8]), 4.5)

    def test_none(self):
        """ Test with no arguments  """
        self.assertEqual(max_integer(), None)

    def test_too_many(self):
        """ Test with too many arguments """
        with self.assertRaises(TypeError):
            max_integer([1, -2, 6, -4], [3, 4, 5, -6])

    def test_nonint(self):
        """ Test with a non-int """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "tralala", -4])

if __name__ == '__main__':
    unittest.main()
