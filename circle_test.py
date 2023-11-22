import math
import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_zero_mult(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_default_mult(self):
        res = circle.area(45)
        self.assertEqual(res, 45*45*math.pi)

    def test_negative_mult(self):
        try:
            res = circle.area(-45)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_mult(self):
        try:
            res = circle.area('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_default_perimeter(self):
        res = circle.perimeter(45)
        self.assertEqual(res, 2*45*math.pi)

    def test_negative_perimeter(self):
        try:
            res = circle.perimeter(-45)
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : negative")

    def test_string_perimeter(self):
        try:
            res = circle.perimeter('10')
        except Exception as e:
            res = e.__class__
        self.assertEqual(res, TypeError, "Incorrect input : string")

    def test_too_much_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter('10', 34)

    def test_too_few_arguments_perimeter(self):
        with self.assertRaises(TypeError):
            res = circle.perimeter()

    def test_too_much_arguments_area(self):
        with self.assertRaises(TypeError):
            res = circle.area('10', 34)

    def test_too_few_arguments_area(self):
        with self.assertRaises(TypeError):
            res = circle.area()
