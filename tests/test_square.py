import sys
sys.path.append('../')

import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("5")

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter("10")

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("10", 5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)

    def test_area_positive(self):
        self.assertEqual(area(4), 16)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(8), 32)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-4)

    def test_large_values(self):
        self.assertEqual(area(1e6), 1e12)
        self.assertEqual(perimeter(1e6), 4e6)

if __name__ == '__main__':
    unittest.main()

