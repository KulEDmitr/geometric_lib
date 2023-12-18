import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
    def test_normal_perimeter(self):
        res = perimeter(10, 5, 7)
        self.assertEqual(res, 22)

    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_string_input_area(self):
        res = area('10', '10')
        self.assertEqual(res, 50)
    def test_string_input_perimeter(self):
        res = perimeter('10', '5', '7')
        self.assertEqual(res, 22)

    def test_math_expression_as_string_input_area(self):
        res = area('2 * 5', '20 / 2')
        self.assertEqual(res, 50)
    def test_math_expression_as_string_input_perimeter(self):
        res = perimeter('5 * 2', '10 / 2', '21 / 3')
        self.assertEqual(res, 22)

    def test_zero_string_input_area(self):
        res = area('', '')
        self.assertEqual(res, 0)
    def test_zero_string_input_perimeter(self):
        res = perimeter('', '', '')
        self.assertEqual(res, 0)


