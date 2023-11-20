import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_string_type_area(self):
        self.assertEqual(area("5", 10), 25)
        self.assertEqual(area("10", 10), 50)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5, 10)
        self.assertRaises(ValueError, area, "-5", 10)

    def test_zero_area(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area("0", "5"), 0)

    def test_area(self):
        self.assertEqual(area(5, 10), 25)
        self.assertEqual(area(10, 10), 50)

    def test_string_type_perimeter(self):
        self.assertEqual(perimeter("5", 10, 12), 27)
        self.assertEqual(perimeter("10", 12, 15), 37)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5, 10, 12)
        self.assertRaises(ValueError, perimeter, "-5", 10, 12)
        self.assertRaises(ValueError, perimeter, 5, 10, 16)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 10, 12), 0)
        self.assertEqual(perimeter("0", "10", "12"), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 10, 12), 27)
        self.assertEqual(perimeter(10, 12, 15), 37)
