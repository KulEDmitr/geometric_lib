from triangle import *
import unittest


class TestTriangleFunctions(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(100, 2), 100)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 2, 100), 105)

    def test_area_negative_first(self):
        self.assertEqual(area(-1, 100_000_000), -1)

    def test_area_negative_second(self):
        self.assertEqual(area(100_000_000, -1), -2)

    def test_perimeter_negative_first(self):
        self.assertEqual(perimeter(-1, 100_000_000, 100_000_000), -1)

    def test_perimeter_negative_second(self):
        self.assertEqual(perimeter(100_000_000, -1, 100_000_000), -2)

    def test_perimeter_negative_third(self):
        self.assertEqual(perimeter(100_000_000, 100_000_000, -1), -3)

    def test_area_large(self):
        self.assertEqual(area(1_000_000_000, 5_000_000_000), 2.5 * 10 ** 18)

    def test_perimeter_large(self):
        self.assertEqual(perimeter(1_000_000_000, 5_000_000_000, 3_123_000_000), 9_123_000_000)
