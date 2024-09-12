import rectangle
import unittest
import math

class RectangleAreaTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = rectangle.area(5, 6)
        self.assertEqual(res, 30)
    def test_float_argument(self):
        res = rectangle.area(4.1, 3.2)
        self.assertEqual(res, 13.12)
    def test_string_argument(self):
        self.assertRaises(TypeError,rectangle.area, "5", 6)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = rectangle.perimeter(4, 5)
        self.assertEqual(res, 18)
    def test_float_argument(self):
        res = rectangle.perimeter(3.28, 6.14)
        self.assertEqual(res, 18.84)
    def test_string_argument(self):
        self.assertRaises(TypeError,rectangle.perimeter, "6", 5)

