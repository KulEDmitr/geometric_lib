from circle import *
import unittest


class TestCircleFunctions(unittest.TestCase):
    def test_area_positive(self):
        self.assertAlmostEqual(area(3), 28.274333882308138)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(perimeter(3), 18.84955592153876)

    def test_area_negative(self):
        self.assertEqual(area(-1), -1)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-1), -1)

    def test_area_large(self):
        self.assertAlmostEqual(area(1_000_000_000), math.pi * 10 ** 18)

    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(1_000_000_000), 6_283_185_307.179586)
