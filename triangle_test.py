import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_zero_mult(self):
        res = triangle.area(0, 3)
        self.assertEqual(res, 0)

    def test_default_mult(self):
        res = triangle.area(45, 3)
        self.assertEqual(res, 45*3 * 0.5)

    def test_negative_mult(self):
        try:
            res = triangle.area(-45, 1)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_mult(self):
        try:
            res = triangle.area('10', 2)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_default_perimeter(self):
        res = triangle.perimeter(45, 3, 23)
        self.assertEqual(res, 45+3+23)

    def test_negative_perimeter(self):
        try:
            res = triangle.perimeter(-45, 3, 45)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_perimeter(self):
        try:
            res = triangle.perimeter('10', 3, 5)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_too_much_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter('10', 25, 3, 5)

    def test_too_few_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = triangle.perimeter(10)

    def test_too_much_arguments_area(self):
        with self.assertRaises(TypeError):
            res = triangle.area('10', 34, 34)

    def test_too_few_arguments_area(self):
        with self.assertRaises(TypeError):
            res = triangle.area('23')