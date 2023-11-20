import sys
sys.path.append('../')
from rectangle import *
import unittest

class TestRectangleFunctions(unittest.TestCase):

    def test_area_positive_sides(self):
        self.assertEqual(area(4.5, 2.7), 4.5 * 2.7)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_large_sides(self):
        self.assertEqual(area(100, 50), 100 * 50)

    def test_area_negative_sides(self):
        self.assertEqual(area(-4.5, 2.7), -4.5 * 2.7)

    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(4.5, 2.7), 2 * (4.5 + 2.7))

    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_large_sides(self):
        self.assertEqual(perimeter(100, 50), 2 * (100 + 50))

    def test_perimeter_negative_sides(self):
        self.assertEqual(perimeter(-4.5, 2.7), 2 * (-4.5 + 2.7))

    def test_area_perimeter_relation(self):
        side_a = 4.5
        side_b = 2.7
        rectangle_area = area(side_a, side_b)
        rectangle_perimeter = perimeter(side_a, side_b)
        self.assertAlmostEqual(rectangle_area / rectangle_perimeter, side_b * side_a / (2 * (side_b + side_a)))

    def test_perimeter_area_relation(self):
        side_a = 4.5
        side_b = 2.7
        rectangle_area = area(side_a, side_b)
        rectangle_perimeter = perimeter(side_a, side_b)
        self.assertAlmostEqual(rectangle_perimeter / rectangle_area, 2 * (side_b + side_a) / (side_b * side_a))
        
    def test_area_output(self):
        self.assertEqual(area(4.5, 2.7), 12.15)

    def test_perimeter_output(self):
        self.assertEqual(perimeter(4.5, 2.7), 14.4)

if __name__ == '__main__':
    unittest.main()
