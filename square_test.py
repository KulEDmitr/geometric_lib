import unittest

from square import *

class SquareTest(unittest.TestCase):

    def test_area_integers(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(area(3), 3 * 3)
        self.assertEqual(area(15), 15 * 15)

    def test_perimeter_integers(self):
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(6), 4 * 6)
        self.assertEqual(perimeter(18), 4 * 18)

    def test_area_non_integers(self):
        self.assertEqual(area(0.3), 0.3 * 0.3)
        self.assertEqual(area(1.25), 1.25 * 1.25)

    def test_perimeter_non_integers(self):
        self.assertEqual(perimeter(4.6), 4 * 4.6)
        self.assertEqual(perimeter(1.8), 4 * 1.8)

    def test_area_processing_values(self):
        self.assertEqual(area('1'), "enter a number")
        self.assertEqual(area('p'), "enter a number")
        self.assertEqual(area(-19), "negative numbers are not allowed")

    def test_perimeter_processing_values(self):
        self.assertEqual(perimeter('i'), "enter a number")
        self.assertEqual(perimeter(-8), "negative numbers are not allowed")


if __name__ == '__main__':
    unittest.main()