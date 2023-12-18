import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_string_input_area(self):
        res = area(10, '10')
        self.assertEqual(res, 100)
    def test_string_input_perimeter(self):
        res = perimeter(10, '10')
        self.assertEqual(res, 40)

    def test_math_expression_as_string_input_area(self):
        res = area('10 / 5', '2 * 7')
        self.assertEqual(res, 28)
    def test_math_expression_as_string_input_perimeter(self):
        res = perimeter('10 / 5', '2 * 7')
        self.assertEqual(res, 32)

    def test_zero_string_input_area(self):
        res = area(12, '')
        self.assertEqual(res, 0)
    def test_zero_string_input_perimeter(self):
        res = perimeter(12, '')
        self.assertEqual(res, 0)
