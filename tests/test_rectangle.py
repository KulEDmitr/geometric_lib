import sys
sys.path.append('../')

import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_invalid_type_area(self):
        with self.assertRaises(TypeError):
            area("5", 3)

    def test_invalid_type_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(5, "3")
    
    def test_area_positive(self):
        self.assertEqual(area(5, 3), 15)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(5, 3), 16)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 3)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 3)

    def test_large_values(self):
        self.assertEqual(area(1e6, 1e6), 1e12)
        self.assertEqual(perimeter(1e6, 1e6), 4e6)

if __name__ == '__main__':
    unittest.main()

