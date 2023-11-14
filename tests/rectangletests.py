import unittest
from geometric_lib.rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    
    def test_area(self):
        self.assertEqual(area(1_000_000, 1_000_000), 1000000000000)
        self.assertEqual(area(8, 8), 64)
        self.assertEqual(area(1, 1), 1)
        self.assertEqual(area(0.1, 0.25), 0.025)
        self.assertEqual(area(0.000924, 6.6162), 0.0061133688)

    def test_zero_area(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_value_area(self):
        self.assertRaises(ValueError, area, -2, 1)
        self.assertRaises(ValueError, area, 4, -2)
        self.assertRaises(ValueError, area, -1000, 2)
    
    def test_types_area(self):
        self.assertRaises(TypeError, area, 'a', 2)
        self.assertRaises(TypeError, area, 'a', True)
        self.assertRaises(TypeError, area, 4, [1, 3, 2])
        self.assertRaises(TypeError, area, (1), '2')
        self.assertRaises(TypeError, area, "Hello", "World")

    def test_perimetr(self):
        self.assertEqual(perimeter(1_000_000, 1_000_000), 4_000_000)
        self.assertEqual(perimeter(8, 8), 32)
        self.assertEqual(perimeter(1, 1), 4)
        self.assertEqual(perimeter(0.18, 2.12), 4.6)
        self.assertEqual(perimeter(9.931, 3.12), 26.102)
    def test_zero_perimeter(self):
        self.assertRaises(ValueError, perimeter, 10, 0)
        self.assertRaises(ValueError, perimeter, 0, 10)
        self.assertRaises(ValueError, perimeter, 0, 0)
    
    def test_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -2, 1)
        self.assertRaises(ValueError, perimeter, 4, -2)
        self.assertRaises(ValueError, perimeter, -1000, 2)
    
    def test_types_perimeter(self):
        self.assertRaises(TypeError, perimeter, '4', '2')
        self.assertRaises(TypeError, perimeter, 'a', 2)
        self.assertRaises(TypeError, perimeter, 'a', True)
        self.assertRaises(TypeError, perimeter, 4, [1, 3, 2])
