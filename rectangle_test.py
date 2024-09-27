import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mult(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_default_mult(self):
        res = rectangle.area(45, 45)
        self.assertEqual(res, 45*45)

    def test_negative_mult(self):
        try:
            res = rectangle.area(-45, 23)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_mult(self):
        try:
            res = rectangle.area('10', 10)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_default_perimeter(self):
        res = rectangle.perimeter(45, 45)
        self.assertEqual(res, 45*4)

    def test_negative_perimeter(self):
        try:
            res = rectangle.perimeter(-45, 2)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_perimeter(self):
        try:
            res = rectangle.perimeter('10', 4)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_too_much_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter('10', 34, 25)

    def test_too_few_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = rectangle.perimeter()

    def test_too_much_arguments_area(self):
        with self.assertRaises(TypeError):
            res = rectangle.area('10', 34, 3)

    def test_too_few_arguments_area(self):
        with self.assertRaises(TypeError):
            res = rectangle.area()