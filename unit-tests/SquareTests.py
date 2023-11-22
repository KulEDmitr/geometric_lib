import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):

    def test_area_null(self):
        self.assertTrue(area(0) == 0)

    def test_area_equal(self):
        self.assertTrue(area(10) == 100)
        self.assertEqual(area(3), 9)

    def test_area_not_equal(self):
        self.assertNotEqual(area(7),47)
        self.assertFalse(area(10) == 10)

    def test_area_string(self):
        self.assertRaises(TypeError, area, "abc",)

    def test_area_negative(self):
        self.assertEqual(area(-1), "the value of the input parameters cannot be negative")

    def test_perimeter_null(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_equal(self):
        self.assertEqual(perimeter(4), 16)
        self.assertTrue(perimeter(1) == 4)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(perimeter(5), 25)
        self.assertFalse(perimeter(10) == 100)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "n")

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-1), "the value of the input parameters cannot be negative")
