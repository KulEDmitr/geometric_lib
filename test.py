import unittest
import math
from rectangle import area as rectangle_area
from circle import area as circle_area
from square import area as square_area
from triangle import area as triangle_area

from rectangle import perimeter as rectangle_perimeter
from circle import perimeter as circle_perimeter
from square import perimeter as square_perimeter
from triangle import perimeter as triangle_perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle_area(0, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle_area(1, 1)
        self.assertEqual(res, 1)

    def test_big_mul(self):
        res = rectangle_area(100000, 1000000)
        self.assertEqual(res, 100000000000)

    def test_negative_mul(self):
        res = rectangle_area(-100000, 1000000)
        self.assertEqual(res, 0)

    def test_perimeter_negative_mul(self):
        res = rectangle_perimeter(-100000, 1000000)
        self.assertEqual(res, 0)

    def test_perimeter_big_mul(self): #2(a+b)
        res = rectangle_perimeter(100000, 1000000)
        self.assertEqual(res, 2*(1000000+100000))

    def test_perimeter_zero_mul(self):
        res = rectangle_perimeter(4, 0)
        self.assertEqual(res, 2*(4+0))

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square_area(10)
        self.assertEqual(res, 0)
    def test_square_mul(self):
        res = square_area(100)
        self.assertEqual(res, 10000)

    def test_negative_mul(self):
        res = square_area(-1000)
        self.assertEqual(res, 0)

    def test_perimeter_zero_mul(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_default_mul(self):
        res = square_perimeter(10)
        self.assertEqual(res, 4*10)

    def test_perimeter_negative_mul(self):
        res = square_perimeter(-10)
        self.assertEqual(res, 0)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = triangle_area(100, 100)
        self.assertEqual(res, 5000)

    def test_perimeter_mul(self):
        res = triangle_perimeter(100, 100, 100)
        self.assertEqual(res, 300)

    def test_perimeter_one_zero_mul(self):
        res = triangle_perimeter(100, 100, 0)
        self.assertEqual(res, 200)

    def test_perimeter_zero_mul(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = circle_area(10)
        self.assertEqual(res, math.pi*10*10)

    def test_negative_mul(self):
        res = circle_area(-10)
        self.assertEqual(res, math.pi * (-10) * (-10))

    def test_perimeter_default_mul(self):
        res = circle_perimeter(10)
        self.assertEqual(res, 2 * math.pi * 10)

    def test_perimeter_zero_mul(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 2 * math.pi * 0)

    def test_perimeter_negative_mul(self):
        res = circle_perimeter(-10)
        self.assertEqual(res, 0)




