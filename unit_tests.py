import unittest

from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

import math

class RectangleTestCase(unittest.TestCase):

    def test_rect_area_common_situation(self):
       result = rect_area(10, 20)
       self.assertEqual(result, 200)

    def test_rect_area_zero_mul(self):
        result = rect_area(10, 0)
        self.assertEqual(result, 0)

    def test_rect_area_neg_mul(self):
        result = rect_area(10, -20)
        self.assertEqual(result, 0)

    def test_rect_area_float_mul(self):
        result = rect_area(10, 2.5)
        self.assertEqual(result, 25)

    def test_rect_perimetr_common_situation(self):
       result = rect_perimeter(10, 20)
       self.assertEqual(result, 200)

    def test_rect_perimetr_zero_mul(self):
        result = rect_perimeter(10, 0)
        self.assertEqual(result, 0)

    def test_rect_perimetr_neg_mul(self):
        result = rect_perimeter(10, -20)
        self.assertEqual(result, 0)

    def test_rect_perimetr_float_mul(self):
        result = rect_perimeter(10, 2.5)
        self.assertEqual(result, 25)

class SquareTestCase(unittest.TestCase):
    def test_square_area_common_situation(self):
        result = square_area(5)
        self.assertEqual(result, 25)

    def test_square_area_zero_mul(self):
        result = square_area(0)
        self.assertEqual(result, 0)

    def test_square_area_neg_mul(self):
        result = square_area(-20)
        self.assertEqual(result, 0)

    def test_square_area_float_mul(self):
        result = square_area(2.5)
        self.assertEqual(result, 6.25)

    def test_square_perimeter_common_situation(self):
        result = square_perimeter(10, 20)
        self.assertEqual(result, 60)

    def test_square_perimeter_zero_mul(self):
        result = square_perimeter(0, 10)
        self.assertEqual(result, 0)

    def test_square_perimeter_neg_mul(self):
        result = square_perimeter(-20, 10)
        self.assertEqual(result, 0)

    def test_square_perimeter_float_mul(self):
        result = square_perimeter(3.5, 5)
        self.assertEqual(result, 17)

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_common_situation(self):
        result = triangle_area(10, 5)
        self.assertEqual(result, 25)

    def test_triangle_area_zero_mul(self):
        result = triangle_area(0, 10)
        self.assertEqual(result, 0)

    def test_triangle_area_neg_mul(self):
        result = triangle_area(-20, 10)
        self.assertEqual(result, 0)

    def test_triangle_area_float_mul(self):
        result = triangle_area(2.5, 10)
        self.assertEqual(result, 25)

    def test_triangle_perimeter_common_situation(self):
        result = triangle_perimeter(10, 20, 29)
        self.assertEqual(result, 59)

    def test_triangle_perimeter_zero_mul(self):
        result = triangle_perimeter(0, 10, 20)
        self.assertEqual(result, 0)

    def test_triangle_perimeter_neg_mul(self):
        result = triangle_perimeter(-20, 10, 20)
        self.assertEqual(result, 0)

    def test_triangle_perimeter_float_mul(self):
        result = triangle_perimeter(3.5, 5, 7)
        self.assertEqual(result, 15.5)

class CircleTestCase(unittest.TestCase):
    def test_circle_area_common_situation(self):
        result = circle_area(10)
        self.assertEqual(abs(result - 10 * 10 * math.pi) < 0.00001, True)

    def test_circle_area_zero_mul(self):
        result = circle_area(0)
        self.assertEqual(result, 0)

    def test_circle_area_neg_mul(self):
        result = circle_area(-20)
        self.assertEqual(result, 0)

    def test_circle_area_float_mul(self):
        result = circle_area(2.5)
        self.assertEqual(abs(result - 2.5 * 2.5 * math.pi) < 0.00001, True)

    def test_circle_perimeter_common_situation(self):
        result = circle_perimeter(10)
        self.assertEqual(abs(result - 2 * 10 * math.pi) < 0.00001, True)

    def test_circle_perimeter_zero_mul(self):
        result = circle_perimeter(0)
        self.assertEqual(result, 0)

    def test_circle_perimeter_neg_mul(self):
        result = circle_perimeter(-20)
        self.assertEqual(result, 0)

    def test_circle_perimeter_float_mul(self):
        result = circle_perimeter(2.5)
        self.assertEqual(abs(result - 2 * 2.5 * math.pi) < 0.00001, True)

if __name__ == '__main__':
    unittest.main()