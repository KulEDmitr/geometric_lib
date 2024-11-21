import unittest
from square import SquareArea, SquarePerimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_natural_numbers(self):
        res = SquareArea(100)
        self.assertEqual(res, 10000)

    def test_square_area_negative_number(self):
        res = SquareArea(-10)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_square_area_chars(self):
        res = SquareArea("a")
        self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_square_area_big_numbers(self):
        res = SquareArea(90000000000)
        self.assertEqual(res, 8100000000000000000000)

    def test_square_perimeter_natural_numbers(self):
        res = SquarePerimeter(10)
        self.assertEqual(res, 40)

    def test_square_perimeter_negative_number(self):
        res = SquarePerimeter(-10)
        self.assertEqual(res, "Incorrect input! Input numbers should be positive")

    def test_square_perimeter_chars(self):
        res = SquarePerimeter("a")
        self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_square_perimeter_big_numbers(self):
        res = SquarePerimeter(90000000000)
        self.assertEqual(res, 360000000000)