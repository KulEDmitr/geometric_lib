import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_string_type_area(self):
        self.assertEqual(area("5", 10), 50)
        self.assertEqual(area("10", 10), 100)

    def test_wrong_value_area(self):
        self.assertRaises(ValueError, area, -5, 10)
        self.assertRaises(ValueError, area, "-5", 10)

    def test_zero_area(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area("0", "5"), 0)

    def test_area(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(10, 10), 100)

    def test_string_type_perimeter(self):
        self.assertEqual(perimeter("5", 10), 30)
        self.assertEqual(perimeter("10", 10), 40)

    def test_wrong_value_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5, 10)
        self.assertRaises(ValueError, perimeter, "-5", 10)

    def test_zero_perimeter(self):
        self.assertEqual(perimeter(0, 5), 0)
        self.assertEqual(perimeter("0", "5"), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(10, 10), 40)
