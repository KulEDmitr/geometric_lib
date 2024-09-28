import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)

    def test_area_zero_area(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, rectangle.area, -1, -2)


    def test_default_perimeter(self):
        res = rectangle.perimeter(5, 8)
        self.assertEqual(res, 26)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, rectangle.perimeter, -3, -7)