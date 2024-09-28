import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(4, 3), 6)
        self.assertEqual(area(0.5, 0.8), 0.2)

    def test_area_zero_value(self):
        self.assertEqual(area(0, 3), 0.0)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(2, 3, 4), 9)
        self.assertEqual(perimeter(0.5, 1.15, 1.2), 2.85)


