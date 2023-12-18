import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_string_input_area(self):
        res = area('10')
        self.assertEqual(res, 100)
    def test_string_input_perimeter(self):
        res = perimeter('10')
        self.assertEqual(res, 40)

    def test_math_expression_as_string_input_area(self):
        res = area('2 * 5')
        self.assertEqual(res, 100)
    def test_math_expression_as_string_input_perimeter(self):
        res = perimeter('5 * 2')
        self.assertEqual(res, 40)

    def test_zero_string_input_area(self):
        res = area('')
        self.assertEqual(res, 0)
    def test_zero_string_input_perimeter(self):
        res = perimeter('')
        self.assertEqual(res, 0)

