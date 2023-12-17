import unittest
from main import area, perimeter


class MyTestCase(unittest.TestCase):
    def test_zero_area(self):
        answer = area(0, 5)
        self.assertEqual(answer, 0)

    def test_triangle_area(self):
        answer = area(2, 5)
        self.assertEqual(answer, 5)

    def test_negative_area(self):
        try:
            answer = area(2, -5)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_string_area(self):
        try:
            answer = area("2", "5")
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_int_string_area(self):
        try:
            answer = area("5", 2)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_zero_perimeter(self):
        answer = perimeter(0, 0, 0)
        self.assertEqual(answer, 0)

    def test_rectangle_perimeter(self):
        answer = perimeter(2, 5, 4)
        self.assertEqual(answer, 11)

    def test_negative_perimeter(self):
        try:
            answer = perimeter(-2, 5, 4)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_string_perimeter(self):
        try:
            answer = perimeter("2", "5", "4")
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_int_string_perimeter(self):
        try:
            answer = perimeter(5, "2", 4)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")
