import sys
sys.path.append('../')
import unittest
from circle import *
import math

class TestCircleFunctions(unittest.TestCase):

    def test_area_positive_radius(self):
        self.assertEqual(area(2.5), math.pi * 2.5 * 2.5)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_area_large_radius(self):
        self.assertAlmostEqual(area(100), math.pi * 100 * 100)

    def test_area_negative_radius(self):
        with self.assertRaises(TypeError):
            area(-2.5)

    def test_perimeter_positive_radius(self):
        self.assertEqual(perimeter(3.5), 2 * math.pi * 3.5)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_large_radius(self):
        self.assertAlmostEqual(perimeter(100), 2 * math.pi * 100)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(TypeError):
            perimeter(-3.5)

    def test_area_perimeter_relation(self):
        radius = 2.5
        circle_area = area(radius)
        circle_perimeter = perimeter(radius)
        self.assertAlmostEqual(circle_area / circle_perimeter, radius / 2)

    def test_perimeter_area_relation(self):
        radius = 3.5
        circle_area = area(radius)
        circle_perimeter = perimeter(radius)
        self.assertAlmostEqual(circle_perimeter / circle_area, 2 / radius)
        
    def test_area_output(self):
        self.assertEqual(area(2.5), 19.634954084936208)

    def test_perimeter_output(self):
        self.assertEqual(perimeter(3.5), 21.991148575128552)

if __name__ == '__main__':
    unittest.main()

