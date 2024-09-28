import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = triangle.area(5, 12)
        self.assertEqual(res, 30)

    def test_area_zero_area(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, triangle.area, -234, -35)

    def test_default_perimeter(self):
        res = triangle.perimeter(41, 35, 27)
        self.assertEqual(res, 38745)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, triangle.perimeter, -9, -2, -17)
