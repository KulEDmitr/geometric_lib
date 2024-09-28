import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_default_area(self):
        res = square.area(6)
        self.assertEqual(res, 36)

    def test_area_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, square.area, -8)


    def test_default_perimeter(self):
        res = square.perimeter(7)
        self.assertEqual(res, 42)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, square.perimeter, -9)
