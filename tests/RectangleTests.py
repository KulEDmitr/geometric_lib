import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_null(self):
        self.assertTrue(area(0, 2) == 0)
        self.assertEqual(area(2, 0), 0)

    def test_area_equal(self):
        self.assertTrue(area(2, 5) == 10)
        self.assertEqual(area(3, 4), 12)

    def test_area_not_equal(self):
        self.assertNotEqual(area(7, 7),47 )
        self.assertFalse(area(10, 2) == 102)

    def test_area_string(self):
        self.assertRaises(TypeError, area, "abc", "def")

    def test_area_negative(self):
        self.assertEqual(area(-1,1), "the value of the input parameters cannot be negative")

    def test_perimeter_null(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(0, 3), 3)

    def test_perimeter_equal(self):
        self.assertEqual(perimeter(1000,2), 2004)
        self.assertTrue(perimeter(1,3) == 8)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(perimeter(5,4), 20)
        self.assertFalse(perimeter(10,1) == 101)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "n", "k")

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-1,1), "the value of the input parameters cannot be negative")
