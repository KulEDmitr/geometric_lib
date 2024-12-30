from rectangle import *
import unittest


class TestRectangleFunctions(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(area(3, 2), 6)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(3, 2), 10)

    def test_area_negative_first(self):
        self.assertEqual(area(-1, 100_000_000), -1)

    def test_area_negative_second(self):
        self.assertEqual(area(100_000_000, -1), -2)

    def test_perimeter_negative_first(self):
        self.assertEqual(perimeter(-1, 100_000_000), -1)

    def test_perimeter_negative_second(self):
        self.assertEqual(perimeter(100_000_000, -1), -2)

    def test_area_large(self):
        self.assertEqual(area(1_000_000_000_000, 1_000_000_000_000), 1_000_000_000_000_000_000_000_000)

    def test_perimeter_large(self):
        self.assertEqual(perimeter(1_000_000_000_000, 1_000_000_000_000), 4_000_000_000_000)
