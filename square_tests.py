from square import *
import unittest


class TestSquareFunctions(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(3), 9)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3), 12)

    def test_area_negative(self):
        self.assertEqual(area(-1), -1)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-1), -1)

    def test_area_large(self):
        self.assertAlmostEqual(area(1_000_000_000_000), 1_000_000_000_000_000_000_000_000)

    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(1_000_000_000_000), 4_000_000_000_000)
