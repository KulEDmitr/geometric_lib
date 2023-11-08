import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertFalse(circle.perimeter(0) == 10)
        self.assertFalse(circle.area(0) == 3)

    def test_default(self):
        self.assertEqual(circle.area(5), 25 * math.pi)
        self.assertEqual(circle.perimeter(5), 10 * math.pi)
        self.assertTrue(circle.area(5) == 25 * math.pi)
        self.assertTrue(circle.perimeter(5) == 10 * math.pi)
        self.assertFalse(circle.area(5) == 25 * 3.14)
        self.assertFalse(circle.perimeter(5) == 10 * 3.14)
