import math
from rectangle import *
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(2, 4)
        self.assertEqual(res, 8)
    def test_int_perimeter(self):
        res = perimeter(2, 4)
        self.assertEqual(res, 12)

    def test_str_area(self):
        res = area('hi', 1)
        self.assertEqual(res, 'Incorrect input')
    def test_str_perimeter(self):
        res = perimeter('hi', 1)
        self.assertEqual(res, 'Incorrect input')

    def test_negative_area(self):
        res = area(-2, 4)
        self.assertEqual(res, 'Incorrect input')
    def test_negative_perimeter(self):
        res = perimeter(-2, 4)
        self.assertEqual(res, 'Incorrect input')

    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
