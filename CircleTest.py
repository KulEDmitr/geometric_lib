import circle
import unittest
import math

class CircleAreaTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_float_argument(self):
        res = circle.area(4.1)
        self.assertEqual(res, 52.81017250684441)
    def test_string_argument(self):
        self.assertRaises(TypeError,circle.area, "5")


class CirclePerimeterTestCase(unittest.TestCase):
    def test_normal_argument(self):
        res = circle.perimeter(4)
        self.assertEqual(res, 25.132741228718345)
    def test_float_argument(self):
        res = circle.perimeter(3.28)
        self.assertEqual(res, 20.60884780754904)
    def test_string_argument(self):
        self.assertRaises(TypeError,circle.perimeter, "6")

