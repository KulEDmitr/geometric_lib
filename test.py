import unittest
import rectangle, square, triangle, circle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(0, 1)
        self.assertEqual(res, 0)
        res = rectangle.area(1, 0)
        self.assertEqual(res, 0)
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = rectangle.area(2, 2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = rectangle.area(0.5, 0.5)
        self.assertEqual(res, 0.25)

    def test_third_area(self):
        res = rectangle.area(0.332, 3)
        self.assertEqual(res, 0.996)

    def test_big1_area(self):
        res = rectangle.area(12345, 2)
        self.assertEqual(res, 24690)

    def test_big2_area(self):
        res = rectangle.area(1020, 1020)
        self.assertEqual(res, 1040400)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)
        res = rectangle.perimeter(0 , 1)
        self.assertEqual(res, 2)
        res = rectangle.perimeter(1, 0)
        self.assertEqual(res, 2)

    def test_one_perimeter(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = rectangle.perimeter(2, 1)
        self.assertEqual(res, 6)

    def test_half_perimeter(self):
        res = rectangle.perimeter(0.5, 0.5)
        self.assertEqual(res, 2)

    def test_third_perimeter(self):
        res = rectangle.perimeter(0.333, 1)
        self.assertEqual(res, 2.666)

    def test_big1_perimeter(self):
        res = rectangle.perimeter(12345, 1242)
        self.assertEqual(res, 27174)

    def test_big2_perimeter(self):
        res = rectangle.perimeter(1020, 1021)
        self.assertEqual(res, 4082)

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = square.area(1)
        self.assertEqual(res, 1)

    def test_two_square_area(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_half_area(self):
        res = square.area(0.5)
        self.assertEqual(res, 0.25)

    def test_small_area(self):
        res = square.area(0.02)
        self.assertEqual(res, 0.0004)

    def test_big1_area(self):
        res = square.area(12345)
        self.assertEqual(res, 152399025)

    def test_big2_area(self):
        res = square.area(1020)
        self.assertEqual(res, 1040400)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)

    def test_two_perimeter(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)

    def test_half_perimeter(self):
        res = square.perimeter(0.5)
        self.assertEqual(res, 2)

    def test_third_perimeter(self):
        res = square.perimeter(0.333)
        self.assertEqual(res, 1.332)

    def test_big1_perimeter(self):
        res = square.perimeter(12345)
        self.assertEqual(res, 49380)

    def test_big2_perimeter(self):
        res = square.perimeter(1020)
        self.assertEqual(res, 4080)

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle.area(0, 1)
        self.assertEqual(res, 0)
        res = triangle.area(1, 0)
        self.assertEqual(res, 0)
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = triangle.area(1, 1)
        self.assertEqual(res, 0.5)

    def test_two_triangle_area(self):
        res = triangle.area(1, 2)
        self.assertEqual(res, 1)

    def test_half_area(self):
        res = triangle.area(0.5, 8)
        self.assertEqual(res, 2)

    def test_small_area(self):
        res = triangle.area(0.02, 0.1)
        self.assertEqual(res, 0.001)

    def test_big1_area(self):
        res = triangle.area(12345, 241)
        self.assertEqual(res, 1487572.5)

    def test_big2_area(self):
        res = triangle.area(1020, 20)
        self.assertEqual(res, 10200)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_two_perimeter(self):
        res = triangle.perimeter(2, 1, 2)
        self.assertEqual(res, 5)

    def test_half_perimeter(self):
        res = triangle.perimeter(0.5, 1, 1.5)
        self.assertEqual(res, 3)

    def test_third_perimeter(self):
        res = triangle.perimeter(0.333, 0.1, 0.2)
        self.assertEqual(res, 0.633)

    def test_big1_perimeter(self):
        res = triangle.perimeter(12345, 123, 7432)
        self.assertEqual(res, 19900)

    def test_big2_perimeter(self):
        res = triangle.perimeter(1020, 1, 10235)
        self.assertEqual(res, 11256)

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = circle.area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_two_area(self):
        res = circle.area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_half_area(self):
        res = circle.area(0.5)
        self.assertEqual(res, 0.7853981633974483)

    def test_third_area(self):
        res = circle.area(0.333)
        self.assertEqual(res, 0.3483680677639186)

    def test_big1_area(self):
        res = circle.area(12345)
        self.assertEqual(res, 478775657.3542472)

    def test_big2_area(self):
        res = circle.area(1020)
        self.assertEqual(res, 3268512.9967948208)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = circle.perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_two_perimeter(self):
        res = circle.perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_half_perimeter(self):
        res = circle.perimeter(0.5)
        self.assertEqual(res, 3.141592653589793)

    def test_third_perimeter(self):
        res = circle.perimeter(0.333)
        self.assertEqual(res, 2.092300707290802)

    def test_big1_perimeter(self):
        res = circle.perimeter(12345)
        self.assertEqual(res, 77565.92261713199)

    def test_big2_perimeter(self):
        res = circle.perimeter(1020)
        self.assertEqual(res, 6408.849013323178)