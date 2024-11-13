import sys
sys.path.append('../')

import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("10", 5)

    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter(3, "4", 5)

    def test_area_positive(self):
        self.assertEqual(area(5, 3), 7.5)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 3)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_large_values(self):
        self.assertEqual(area(1e6, 1e6), 5e11)
        self.assertEqual(perimeter(1e6, 1e6, 1e6), 3e6)

if __name__ == '__main__':
    unittest.main()

