import sys
sys.path.append('../')
from triangle import *
import unittest

class TestTriangleFunctions(unittest.TestCase):
    def test_area_positive_values(self):
        self.assertAlmostEqual(area(4.5, 2.7), 6.075, places=3)

    def test_area_zero_base(self):
        self.assertAlmostEqual(area(0, 2.7), 0, places=3)

    def test_area_zero_height(self):
        self.assertAlmostEqual(area(4.5, 0), 0, places=3)

    def test_area_negative_values(self):
        self.assertAlmostEqual(area(-4.5, 2.7), -6.075, places=3)

    def test_perimeter_positive_values(self):
        self.assertAlmostEqual(perimeter(4.5, 2.7, 3.8), 11.0, places=3)

    def test_perimeter_zero_sides(self):
        self.assertAlmostEqual(perimeter(0, 0, 0), 0, places=3)

    def test_perimeter_negative_values(self):
        self.assertAlmostEqual(perimeter(-4.5, 2.7, 3.8), 2.0, places=3)

    def test_perimeter_invalid_input(self):
        with self.assertRaises(TypeError):
            perimeter(4.5, 2.7, "3.8")

    def test_area_invalid_input(self):
        with self.assertRaises(TypeError):
            area(4.5, "2.7")

    def test_area_large_values(self):
        self.assertAlmostEqual(area(10**6, 10**6), 5.0e11, places=3)

    def test_perimeter_large_values(self):
        self.assertAlmostEqual(perimeter(10**6, 10**6, 10**6), 3.0e6, places=3)

    def test_area_decimal_values(self):
        self.assertAlmostEqual(area(1.5, 0.5), 0.375, places=3)

    def test_perimeter_decimal_values(self):
        self.assertAlmostEqual(perimeter(1.5, 0.5, 1.0), 3.0, places=3)

    def test_area_negative_base(self):
        self.assertAlmostEqual(area(-4.5, 2.7), -6.075, places=3)

    def test_area_negative_height(self):
        self.assertAlmostEqual(area(4.5, -2.7), -6.075, places=3)

    def test_perimeter_negative_sides(self):
        self.assertAlmostEqual(perimeter(-4.5, 2.7, -3.8), -5.6, places=3)

if __name__ == '__main__':
    unittest.main() 
