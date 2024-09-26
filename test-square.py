import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    def test_zero_value_area(self):
        result = area(0)
        self.assertEqual(result, 0, "Incorrect on zero side in area in square.")

    def test_integer_value_area(self):
        result = area(5)
        self.assertEqual(result, 25, "Incorrect on simple side in area in square.")

    def test_float_value_area(self):
        result = area(2.5)
        self.assertEqual(result, 6.25, "Incorrect on float side in area in square.")

    def test_string_value_area(self):
        try:
            result = area("aaa")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in square.")

    def test_integer_value_perimeter(self):
        result = perimeter(5)
        self.assertEqual(result, 20, "Incorrect on simple side in perimeter in square.")

    def test_zero_value_perimeter(self):
        result = perimeter(0)
        self.assertEqual(result, 0, "Incorrect on zero side in perimeter in square.")

    def test_float_value_perimeter(self):
        result = perimeter(2.5)
        self.assertEqual(result, 10, "Incorrect on float side in area in square.")

    def test_string_value_perimeter(self):
        try:
            result = perimeter("a")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeter in square.")
