import unittest
import triangle


class TriangleTest(unittest.TestCase):
    def test_zero_side(self):
        self.assertFalse(triangle.area(0, 5) == 5)
        self.assertFalse(triangle.area(5, 0), 5)
        self.assertEqual(triangle.perimeter(0, 5, 5), 10)
        self.assertEqual(triangle.perimeter(0, 0, 5), 5)

    def test_default(self):
        self.assertEqual(triangle.area(5, 5), 12.5)
        self.assertEqual(triangle.area(2, 5), 5)
        self.assertEqual(triangle.area(5, 2), 5)
        self.assertTrue(triangle.area(2, 5) == 5)
        self.assertTrue(triangle.area(5, 2) == 5)
        self.assertFalse(triangle.area(1, 2) == 3)
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
        self.assertEqual(triangle.perimeter(2, 1.5, 1), 4.5)
        self.assertEqual(triangle.perimeter(5, 2, 4), 11)
        self.assertTrue(triangle.perimeter(2, 1.5, 1) == 4.5)
        self.assertTrue(triangle.perimeter(5, 2, 4) == 11)
        self.assertFalse(triangle.perimeter(1, 2, 1) == 3)
