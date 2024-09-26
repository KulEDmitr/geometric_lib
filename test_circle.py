import math
from circle import *
import unittest

class CircleTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)
    def test_int_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_str_area(self):
        res = area('hi')
        self.assertEqual(res, 'Incorrect input')
    def test_str_perimeter(self):
        res = perimeter('hi')
        self.assertEqual(res, 'Incorrect input')

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, 'Incorrect input')
    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, 'Incorrect input')

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0.0)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)
