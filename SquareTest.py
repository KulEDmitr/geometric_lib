import square
import unittest
import math

class SquareAreaTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = square.area(5)
        self.assertEqual(res, 25)
    def test_float_argument(self):
        res = square.area(4.1)
        self.assertEqual(res, 16.81)
    def test_string_argument(self):
        self.assertRaises(TypeError,square.area, "5")


class SquarePerimeterTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = square.perimeter(4)
        self.assertEqual(res, 16)
    def test_float_argument(self):
        res = square.perimeter(3.28)
        self.assertEqual(res, 13.12)
    def test_string_argument(self):
        self.assertRaises(TypeError,square.perimeter, "6")
