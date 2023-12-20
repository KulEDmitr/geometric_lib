import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    def test_integer_value_area(self):
        result = area(5, 5)
        self.assertEqual(result, 25, "Incorrect on integer sides in area in rectangle.")

    def test_zero_value_area(self):
        result = area(0, 0)
        self.assertEqual(result, 0, "Incorrect on zero sides in area in rectangle.")

    def test_float_value_area(self):
        result = area(2.5, 2.5)
        self.assertEqual(result, 6.25, "Incorrect on float sides in area in rectangle.")

    def test_string_value_area(self):
        try:
            result = area("a", "b")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in rectangle.")

    def test_one_string_value_area(self):
        try:
            result = area("a", 1)
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in rectangle.")

    def test_integer_value_perimeter(self):
        result = perimeter(25, 25)
        self.assertEqual(result, 100, "Incorrect on integer sides in perimeter in rectangle.")

    def test_float_value_perimeter(self):
        result = perimeter(22.5, 22.5)
        self.assertEqual(result, 90, "Incorrect on float sides in perimeter in rectangle.")

    def test_string_value_perimeter(self):
        try:
            result = perimeter("a", "b")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeter in rectangle.")

    def test_one_string_value_perimeter(self):
        try:
            result = perimeter("a", 1)
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeter in rectangle.")

    def test_zero_value_perimeter(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0, "Incorrect on zero sides in perimeter in rectangle.")
