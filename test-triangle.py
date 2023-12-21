import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_zero_value_area(self):
        result = area(0, 0)
        self.assertEqual(result, 0, "Incorrect on zero side and height in area in triangle.")

    def test_integer_value_area(self):
        result = area(5, 6)
        self.assertEqual(result, 15, "Incorrect on integer side and height in area in triangle.")

    def test_float_value_area(self):
        result = area(2.5, 2.6)
        self.assertEqual(result, 3.25, "Incorrect on float side and height in area in triangle.")

    def test_string_value_area(self):
        try:
            result = area("a", "b")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in triangle.")

    def test_one_string_value_area(self):
        try:
            result = area(6, "a")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in triangle.")

    def test_zero_value_perimeter(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0, "Incorrect on zero all side in perimeter in triangle.")

    def test_integer_value_perimeter(self):
        result = perimeter(5, 6, 7)
        self.assertEqual(result, 18, "Incorrect on simple all side in perimeter in triangle.")

    def test_float_value_perimeter(self):
        result = perimeter(5.5, 6.5, 7.5)
        self.assertEqual(result, 19.5, "Incorrect on float all side in perimeter in triangle.")

    def test_string_value_perimeter(self):
        try:
            result = perimeter("a", "b", "c")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeters in triangle.")

    def test_one_string_value_perimeter(self):
        try:
            result = perimeter("a", 2, 3)
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeters in triangle.")
