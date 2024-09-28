import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_default_area(self):
        res = circle.area(7)
        self.assertEqual(res, circle.math.pi ** 2 * 7)

    def test_area_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_negative_value(self):
        self.assertRaises(ValueError, circle.area, -2)


    def test_default_perimeter(self):
        res = circle.perimeter(5)
        self.assertEqual(res, circle.math.pi * 2 * 5)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, circle.perimeter, -3)
