import unittest
import math
import sys
sys.path.append('../')
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    def test_invalid_type_area(self):
        with self.assertRaises(TypeError):
            area("10")

    def test_invalid_type_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("20")

    def test_area_positive(self):
        self.assertAlmostEqual(area(10), 314.1592653589793)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(8), 50.26548245743669)

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_area_large(self):
        self.assertAlmostEqual(area(1e6), math.pi * (1e6)**2)

    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(1e6), 2 * math.pi * 1e6)

if __name__ == '__main__':
    unittest.main()

