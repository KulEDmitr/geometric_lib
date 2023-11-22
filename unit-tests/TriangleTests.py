import unittest
from triangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_null(self):
        self.assertTrue(area(0, 0, ) == 0)
        self.assertEqual(area(2, 0), 0)

    def test_area_equal(self):
        self.assertTrue(area(2, 5) == 5)
        self.assertEqual(area(3, 4), 6)

    def test_area_not_equal(self):
        self.assertNotEqual(area(7, 6),42 )
        self.assertFalse(area(10, 2) == 100)

    def test_area_string(self):
        self.assertRaises(TypeError, area, "abc", "def")

    def test_area_negative(self):
        self.assertEqual(area(-1,1), "the value of the input parameters cannot be negative")

    def test_perimeter_null(self):
        self.assertEqual(perimeter(0, 0,2), 2)
        self.assertEqual(perimeter(0, 2,2), "there is no triangle with such sides")

    def test_perimeter_equal(self):
        self.assertEqual(perimeter(10,2, 10), 22)
        self.assertTrue(perimeter(3,3, 3) == 9)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(perimeter(5,4,3), 6)
        self.assertFalse(perimeter(1,1, 1) == 111)

    def test_perimeter_string(self):
        self.assertRaises(TypeError, perimeter, "n", "k", "l")

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-1,1, -1), "the value of the input parameters cannot be negative")
