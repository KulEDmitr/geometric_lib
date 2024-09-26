import math
from triangle import *
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(3, 4)
        self.assertEqual(res, 6)
    def test_int_perimeter(self):
        res = perimeter(2, 4, 3)
        self.assertEqual(res, 9)

    def test_str_area(self):
        res = area('hi', 3.4)
        self.assertEqual(res, 'Incorrect input')
    def test_str_perimeter(self):
        res = perimeter('hi', 1, 0.6)
        self.assertEqual(res, 'Incorrect input')

    def test_negative_area(self):
        res = area(-2, 4)
        self.assertEqual(res, 'Incorrect input')
    def test_negative_perimeter(self):
        res = perimeter(-2, 4, 0)
        self.assertEqual(res, 'Incorrect input')

    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_triangle_is_not_exist_perimeter(self):
        res = perimeter(5, 1, 3)
        self.assertEqual(res, 'Incorrect input')
