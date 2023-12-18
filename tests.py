import unittest
import rectangle, square, triangle, circle

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(10, 3)
        self.assertEqual(res, 30)
    def test_area_with_0(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    def test_area_with_1(self):
        res = rectangle.area(10, 1)
        self.assertEqual(res, 10)
    def test_area_float_1(self):
        res = rectangle.area(10, 1.5)
        self.assertEqual(res, 15)
    def test_area_float_2(self):
        res = rectangle.area(2.5, 1.5)
        self.assertEqual(res, 3.75)
    def test_perimeter(self):
        res = rectangle.perimeter(10, 3)
        self.assertEqual(res, 26)
    def test_perimetr_with_0(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
    def test_perimeter_float_1(self):
        res = rectangle.perimeter(10, 1.5)
        self.assertEqual(res, 23)
    def test_perimeter_float_2(self):
        res = rectangle.perimeter(2.5, 1.5)
        self.assertEqual(res, 8)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(10, 3)
        self.assertEqual(res, 15)
    def test_area_with_0(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
    def test_area_with_1(self):
        res = triangle.area(10, 1)
        self.assertEqual(res, 5)
    def test_area_float_1(self):
        res = triangle.area(20, 1.5)
        self.assertEqual(res, 15)
    def test_area_float_2(self):
        res = triangle.area(5, 1.5)
        self.assertEqual(res, 3.75)
    def test_perimeter(self):
        res = triangle.perimeter(10, 5, 3)
        self.assertEqual(res, 18)
    def test_perimetr_with_0(self):
        res = triangle.perimeter(10, 0, 10)
        self.assertEqual(res, 20)
    def test_perimeter_float_1(self):
        res = triangle.perimeter(10, 1.5, 3)
        self.assertEqual(res, 14.5)
    def test_perimeter_float_2(self):
        res = triangle.perimeter(2.5, 1.5, 1)
        self.assertEqual(res, 5)

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_area_with_0(self):
        res = circle.area(0)
        self.assertEqual(res, 0.0)
    def test_area_float(self):
        res = circle.area(1.5)
        self.assertEqual(res, 7.0685834705770345)
    def test_perimeter(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    def test_perimetr_with_0(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0.0)
    def test_perimeter_float(self):
        res = circle.perimeter(1.5)
        self.assertEqual(res, 9.42477796076938)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)
    def test_area_with_0(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    def test_area_float(self):
        res = square.area(1.5)
        self.assertEqual(res, 2.25)
    def test_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
    def test_perimetr_with_0(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    def test_perimeter_float(self):
        res = square.perimeter(1.5)
        self.assertEqual(res, 6)

unittest.main()