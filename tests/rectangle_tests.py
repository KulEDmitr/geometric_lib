import unittest
from rectangle import RectangleArea, RectanglePerimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_natural_numbers(self):
        res = RectangleArea(300, 200)
        self.assertEqual(res, 60000)

    def test_rectangle_area_negative_number(self):
        res = RectangleArea(-100, 40)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_rectangle_area_chars(self):
        res = RectangleArea("a", "b")
        self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_rectangle_area_big_numbers(self):
        res = RectangleArea(9000000000, 8000000000)
        self.assertEqual(res, 72000000000000000000)

    def test_rectangle_perimeter_natural_numbers(self):
        res = RectanglePerimeter(10, 40)
        self.assertEqual(res, 100)

    def test_rectangle_perimeter_negative_number(self):
        res = RectanglePerimeter(-10, 0)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_rectangle_perimeter_chars(self):
        res = RectanglePerimeter("a", 0)
        self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_rectangle_perimeter_big_numbers(self):
        res = RectanglePerimeter(9000000000, 7000000000)
        self.assertEqual(res, 32000000000)