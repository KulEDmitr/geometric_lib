import unittest
from circle import CircleArea, CirclePerimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_natural_numbers(self):
        res = CircleArea(10)
        self.assertEqual(res, 314.1592653589793)

    def test_circle_area_negative_number(self):
        res = CircleArea(-10)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_circle_area_chars(self):
        res = CircleArea("a")
        self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_circle_area_big_numbers(self):
        res = CircleArea(9000000000)
        self.assertEqual(res, 2.5446900494077326e+20)

    def test_circle_perimeter_natural_numbers(self):
        res = CirclePerimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_circle_perimeter_negative_number(self):
        res = CirclePerimeter(-10)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_circle_perimeter_chars(self):
        res = CirclePerimeter("a")
        self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_circle_perimeter_big_numbers(self):
        res = CirclePerimeter(90000000000)
        self.assertEqual(res, 565486677646.1627)