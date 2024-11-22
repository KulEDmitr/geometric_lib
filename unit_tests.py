import unittest
import rectangle
import circle
import square
import triangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_positive_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

class CircleTestCase(unittest.TestCase):
    def test_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_positive_radius(self):
        res = circle.area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 62.83185307179586)

class SquareTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_positive_side(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

class TriangleTestCase(unittest.TestCase):
    def test_zero_sides(self):
        res = triangle.area(0, 2)
        self.assertEqual(res, 0)

    def test_positive_sides(self):
        res = triangle.area(4, 2)
        self.assertEqual(res, 4.0)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
