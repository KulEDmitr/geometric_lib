import unittest

from rectangle import area as RectangleArea
from rectangle import perimeter as RectanglePerimeter
from square import area as SquareArea
from square import perimeter as SquarePerimeter
from triangle import area as TriangleArea
from triangle import perimeter as TrianglePerimeter
from circle import area as CircleleArea
from circle import perimeter as CirclePerimeter


class RectangleTestCase(unittest.TestCase):
    def test_zero_in_mul(self):
        res = RectangleArea(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = RectangleArea(10, 10)
        self.assertEqual(res, 100)

    def test_one_in_mul(self):
        res = RectangleArea(1, 10)
        self.assertEqual(res, 10)

    def test_zero_in_perim(self):
        res = RectanglePerimeter(10, 0)
        self.assertEqual(res, 20)

    def test_equal_perim(self):
        res = RectanglePerimeter(10, 10)
        self.assertEqual(res, 40)

    def test_one_in_perim(self):
        res = RectanglePerimeter(1, 10)
        self.assertEqual(res, 22)


class SquareTestCase(unittest.TestCase):
    def test_zero_in_mul(self):
        res = SquareArea(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = SquareArea(10)
        self.assertEqual(res, 100)

    def test_one_in_mul(self):
        res = SquareArea(1)
        self.assertEqual(res, 1)

    def test_zero_in_perim(self):
        res = SquarePerimeter(0)
        self.assertEqual(res, 0)

    def test_equal_perim(self):
        res = SquarePerimeter(10)
        self.assertEqual(res, 40)

    def test_one_in_perim(self):
        res = SquarePerimeter(1)
        self.assertEqual(res, 4)


class TriangleTestCase(unittest.TestCase):
    def test_zero_in_mul(self):
        res = TriangleArea(0, 5)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = TriangleArea(10, 10)
        self.assertEqual(res, 50)

    def test_one_in_mul(self):
        res = TriangleArea(1, 10)
        self.assertEqual(res, 5)

    def test_zero_in_perim(self):
        res = TrianglePerimeter(0, 1, 2)
        self.assertEqual(res, 3)

    def test_equal_perim(self):
        res = TrianglePerimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_one_in_perim(self):
        res = TrianglePerimeter(1, 5, 5)
        self.assertEqual(res, 11)

class CircleTestCase(unittest.TestCase):
    def test_zero_in_mul(self):
        res = CircleleArea(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = CircleleArea(5)
        self.assertEqual(res, 78.53981633974483)

    def test_one_in_mul(self):
        res = CircleleArea(1)
        self.assertEqual(res, 3.141592653589793)

    def test_zero_in_perim(self):
        res = CirclePerimeter(0)
        self.assertEqual(res, 0)

    def test_equal_perim(self):
        res = CirclePerimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_one_in_perim(self):
        res = CirclePerimeter(1)
        self.assertEqual(res, 6.283185307179586)
