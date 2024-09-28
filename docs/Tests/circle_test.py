import math
import unittest
from circle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(4), math.pi * 16)
        self.assertEqual(area(2), 4 * math.pi)

    def test_area_zero_value(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(2), 4 * math.pi)
        self.assertEqual(perimeter(0.5), math.pi)
