import triangle
import unittest
import math

class TriangleAreaTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = triangle.area(5, 6)
        self.assertEqual(res, 15)
    def test_float_argument(self):
        res = triangle.area(4.1, 3.2)
        self.assertEqual(res, 6.56)
    def test_string_argument(self):
        self.assertRaises(TypeError,triangle.area, "5", 6)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = triangle.perimeter(4, 5, 2)
        self.assertEqual(res, 11)
    def test_float_argument(self):
        res = triangle.perimeter(3.28, 6.14, 1.2)
        self.assertEqual(res, 10.62)
    def test_string_argument(self):
        self.assertRaises(TypeError,triangle.perimeter, "6", 5, "4")

