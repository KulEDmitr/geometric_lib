import unittest
from rectangle import area
from rectangle import perimeter


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 3 * 4)

    def test_pi_area(self):
        self.assertEqual(area(1, 1), 1)

    def test_zero_area(self):
        self.assertEqual(area(0, 3), 0)

    def test_fractional_area(self):
        self.assertEqual(area(5.5, 2), 5.5 * 2)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -2, 3)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 6), 2 * (5+6))

    def test_pi_perimeter(self):
        self.assertEqual(perimeter(1, 1), 2 * (1+1))

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_fractional_perimeter(self):
        self.assertEqual(perimeter(2.5, 5), 2 * (2.5+5))

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3, 4)




