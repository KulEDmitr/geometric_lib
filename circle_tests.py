import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10)
        self.assertEqual(res, 314.159265)
    def test_normal_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.831853)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_string_input_area(self):
        res = area('10')
        self.assertEqual(res, 314.159265)
    def test_string_input_perimeter(self):
        res = perimeter('10')
        self.assertEqual(res, 62.831853)

    def test_math_expression_as_string_input_area(self):
        res = area('5 * 2')
        self.assertEqual(res, 314.159265)
    def test_math_expression_as_string_input_perimeter(self):
        res = perimeter('5 * 2')
        self.assertEqual(res, 62.831853)

    def test_zero_string_input_area(self):
        res = area('')
        self.assertEqual(res, 0)
    def test_zero_string_input_perimeter(self):
        res = perimeter('')
        self.assertEqual(res, 0)

