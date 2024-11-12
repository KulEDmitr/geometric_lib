import unittest
from triangle import TriangleArea, TrianglePerimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_natural_numbers(self):
        res = TriangleArea(10, 15)
        self.assertEqual(res, 75.0)

    def test_triangle_area_negative_numbers(self):
        res = TriangleArea(-10, -3)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_triangle_area_chars(self):
        res = TriangleArea(-10, "a")
        self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_triangle_area_big_numbers(self):
        res = TriangleArea(9000000000, 1000000000)
        self.assertEqual(res, 4500000000000000000)

    def test_triangle_perimeter_natural_numbers(self):
        res = TrianglePerimeter(9, 12, 15)
        self.assertEqual(res, 36)

    def test_triangle_perimeter_negative_number(self):
        res = TrianglePerimeter(-10, 10, -10)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_triangle_perimeter_chars(self):
        res = TrianglePerimeter(3, "a", "b")
        self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_triangle_perimeter_big_numbers(self):
        res = TrianglePerimeter(9000000, 10000000, 10000000)
        self.assertEqual(res, 29000000)