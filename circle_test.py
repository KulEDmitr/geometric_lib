import unittest
from math import pi
from main import area, perimeter


class MyTestCase(unittest.TestCase):
    def test_zero_area(self):
        data = area(0)
        self.assertEqual(data, 0)

    def test_circle_area(self):
        data = area(5)
        self.assertEqual(data, 25 * pi)

    def test_negative_area(self):
        try:
            data = area(-5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Input Error")

    def test_string_area(self):
        try:
            data = area('5')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Input Error")

    def test_zero_perimeter(self):
        data = perimeter(0)
        self.assertEqual(data, 0)

    def test_circle_perimeter(self):
        data = perimeter(5)
        self.assertEqual(data, 10 * pi)

    def test_negative_perimeter(self):
        try:
            data = perimeter(-5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Input Error")

    def test_string_perimeter(self):
        try:
            data = perimeter('5')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Input Error")
