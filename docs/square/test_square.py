import unittest
from square import area
from square import perimeter


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(9), 9 * 9)

    def test_pi_area(self):
        self.assertEqual(area(1), 1)

    def test_zero_area(self):
        self.assertEqual(area(0), 0)

    def test_fractional_area(self):
        self.assertEqual(area(3.25), 3.25 * 3.25)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 4 * 5)

    def test_pi_perimeter(self):
        self.assertEqual(perimeter(1), 4 * 1)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0), 0)

    def test_fractional_perimeter(self):
        self.assertEqual(perimeter(2.5), 4 * 2.5)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2)




