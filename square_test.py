import unittest
from main import area, perimeter

class MyTestCase(unittest.TestCase):
    def test_zero_area(self):
        answer = area(0)
        self.assertEqual(answer, 0)

    def test_square_area(self):
        answer = area(5)
        self.assertEqual(answer, 25)

    def test_negative_area(self):
        try:
            answer = area(-5)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_string_area(self):
        try:
            answer = area("5")
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_zero_perimeter(self):
        answer = perimeter(0)
        self.assertEqual(answer, 0)

    def test_square_perimeter(self):
        answer = perimeter(5)
        self.assertEqual(answer, 20)

    def test_negative_perimeter(self):
        try:
            answer = perimeter(-5)
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")

    def test_string_perimeter(self):
        try:
            answer = perimeter("5")
        except Exception as f:
            answer = f.__class__
        self.assertEqual(answer, TypeError, "Input Error")
