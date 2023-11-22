import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_zero_mult(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_default_mult(self):
        res = square.area(45)
        self.assertEqual(res, 45*45)

    def test_negative_mult(self):
        try:
            res = square.area(-45)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_mult(self):
        try:
            res = square.area('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_default_perimeter(self):
        res = square.perimeter(45)
        self.assertEqual(res, 45*4)

    def test_negative_perimeter(self):
        try:
            res = square.perimeter(-45)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_perimeter(self):
        try:
            res = square.perimeter('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_too_much_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = square.perimeter('10', 25)

    def test_too_few_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = square.perimeter()

    def test_too_much_arguments_area(self):
        with self.assertRaises(TypeError):
            res = square.area('10', 34)

    def test_too_few_arguments_area(self):
        with self.assertRaises(TypeError):
            res = square.area()