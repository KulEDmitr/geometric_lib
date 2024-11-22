import unittest
import math
from circle import area, perimeter


class CircleTestArea(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(area(2), 4 * math.pi)
        self.assertEqual(area(13), 169 * math.pi)
        self.assertEqual(area(0.3), 0.09 * math.pi)
    
    def test_zero_values(self):
        self.assertEqual(area(0), 0)


class CircleTestPerimeter(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(perimeter(2), 4 * math.pi)
        self.assertEqual(perimeter(13), 26 * math.pi)
        self.assertEqual(perimeter(0.3), 0.6 * math.pi)
    
    def test_zero_values(self):
        self.assertEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()