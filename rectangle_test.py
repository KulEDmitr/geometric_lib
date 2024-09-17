import unittest

from rectangle import *

class RectangleTest(unittest.TestCase):

    def test_area_integers(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(8, 3), 8 * 3)
        self.assertEqual(area(92, 15), 92 * 15)

    def test_perimeter_integers(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(6, 4), 2 * (6 + 4))
        self.assertEqual(perimeter(18, 9), 2 * (18 + 9))

    def test_area_non_integers(self):
        self.assertEqual(area(0.8, 3), 0.8 * 3)
        self.assertEqual(area(9.2, 1.5), 9.2 * 1.5)

    def test_perimeter_non_integers(self):
        self.assertEqual(perimeter(9.16, 4.1), 2 * (9.16 + 4.1))
        self.assertEqual(perimeter(1.8, 2.9), 2 * (1.8 + 2.9))

    def test_area_processing_values(self):
        self.assertEqual(area('1', 8), "enter a number")
        self.assertEqual(area('y', 1.8), "enter a number")
        self.assertEqual(area(-19, 8), "negative numbers are not allowed")
        self.assertEqual(area(76, -8.1), "negative numbers are not allowed")

    def test_perimeter_processing_values(self):
        self.assertEqual(perimeter('i', 2), "enter a number")
        self.assertEqual(perimeter(-8, -3), "negative numbers are not allowed")
        self.assertEqual(perimeter(-8, 9.1), "negative numbers are not allowed")

    def test_area_count_values(self):
        self.assertEqual(area(8), "enter 2 values")
        self.assertEqual(area(1.8), "enter 2 values")

    def test_perimeter_count_values(self):
        self.assertEqual(perimeter(2), "enter 2 values")
        self.assertEqual(perimeter(45), "enter 2 values")

if __name__ == '__main__':
    unittest.main()

