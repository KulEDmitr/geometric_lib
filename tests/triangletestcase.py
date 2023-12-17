import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(1, 2), 1)
        self.assertEqual(area(4, 4), 8)
        self.assertEqual(area(3, 7), 10.5)
        self.assertEqual(area(21.16, 0.4), 4.232)

    def test_zero_area(self):
        self.assertEqual(area(0, 8), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_value_area(self):
        self.assertRaises(ValueError, area, -1, 7)
        self.assertRaises(ValueError, area, 9, -18)
        self.assertRaises(ValueError, area, -1.13, 7.1)

    def test_types_area(self):
        self.assertRaises(TypeError, area, [1], 5)
        self.assertRaises(TypeError, area, '1', '5')
        self.assertRaises(TypeError, area, "hello", 5)

    def test_perimeter(self):
        self.assertRaises(ValueError, perimeter, 1, 2, 3)
        self.assertEqual(perimeter(4, 4, 5), 13)
        self.assertEqual(perimeter(7, 8, 3.5), 18.5)
        self.assertEqual(perimeter(3.5, 7.5, 4), 15)
        self.assertRaises(ValueError, perimeter, 7, 2, 3)

    def test_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -1, 7, 9)
        self.assertRaises(ValueError, perimeter, 9, -18, 1.5)
        self.assertRaises(ValueError, perimeter, -1.13, 7.1, 9)
        self.assertRaises(ValueError, perimeter, 0, 8, 1)
        self.assertRaises(ValueError, perimeter, 10, 0, 2)
        self.assertRaises(ValueError, perimeter, 0, 0, 0)

    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, [1], 5, -10)
        self.assertRaises(TypeError, perimeter, '1', '5', 'a')
        self.assertRaises(TypeError, perimeter, "hello", 5, ['pahan'])
