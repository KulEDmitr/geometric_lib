import math
from square import *
import unittest

class SquareTestCase(unittest.TestCase):
    def test_int_area(self):
        res = area(3)
        self.assertEqual(res, 9)
    def test_int_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_str_area(self):
        res = area('5')
        self.assertEqual(res, 'Incorrect input')
    def test_str_perimeter(self):
        res = perimeter('6')
        self.assertEqual(res, 'Incorrect input')

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, 'Incorrect input')
    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, 'Incorrect input')

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
