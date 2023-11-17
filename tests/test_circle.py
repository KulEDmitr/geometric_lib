import unittest
from circle import area, perimeter
import math

class TestCircleModule(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(2), 12.566370614359172, places=8)
        self.assertAlmostEqual(area(5), 78.53981633974483, places=8)
        self.assertAlmostEqual(area(3.5), 38.48451000647496, places=8)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172, places=8)
        self.assertAlmostEqual(perimeter(5), 31.41592653589793, places=8)
        self.assertAlmostEqual(perimeter(3.5), 21.991148575128552, places=8)

    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)

    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)

if __name__ == '__main__':
    unittest.main()
