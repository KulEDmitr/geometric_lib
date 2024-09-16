import unittest
import circle
import rectangle
import triangle
import square


class CircleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        res1 = circle.area(0)
        self.assertEqual(res1, 0)

    def test_zero_mul_perimeter(self):
        res2 = circle.perimeter(0)
        self.assertEqual(res2, 0)

    def test_mul_area(self):
        res1 = circle.area(10)
        self.assertEqual(res1, 314.1592653589793)

    def test_mul_perimeter(self):
        res2 = circle.perimeter(10)
        self.assertEqual(res2, 62.83185307179586)

    def test_big_mul_area(self):
        res1 = circle.area(1000000)
        self.assertEqual(res1, 3141592653589.793)

    def test_big_mul_perimeter(self):
        res2 = circle.perimeter(1000000)
        self.assertEqual(res2, 6283185.307179586)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        res1 = rectangle.area(0, 5)
        self.assertEqual(res1, 0)

    def test_zero_mul_perimeter(self):
        res2 = rectangle.perimeter(0, 7)
        self.assertEqual(res2, 14)

    def test_mul_area(self):
        res1 = rectangle.area(2, 5)
        self.assertEqual(res1, 10)

    def test_mul_perimeter(self):
        res2 = rectangle.perimeter(2, 8)
        self.assertEqual(res2, 20)

    def test_big_mul_area(self):
        res1 = rectangle.area(1000000, 2000000)
        self.assertEqual(res1, 2000000000000)

    def test_big_mul_perimeter(self):
        res2 = rectangle.perimeter(1000000, 20000023)
        self.assertEqual(res2, 42000046)


class SquareTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        res1 = square.area(0)
        self.assertEqual(res1, 0)

    def test_zero_mul_perimeter(self):
        res2 = square.perimeter(0)
        self.assertEqual(res2, 0)

    def test_mul_area(self):
        res1 = square.area(5)
        self.assertEqual(res1, 25)

    def test_mul_perimeter(self):
        res2 = square.perimeter(6)
        self.assertEqual(res2, 24)

    def test_big_mul_area(self):
        res1 = square.area(1000000)
        self.assertEqual(res1, 1000000000000)

    def test_big_mul_perimeter(self):
        res2 = square.perimeter(1000000)
        self.assertEqual(res2, 4000000)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        res1 = triangle.area(0, 56)
        self.assertEqual(res1, 0)

    def test_zero_mul_perimeter(self):
        res2 = triangle.perimeter(0, 1, 2)
        self.assertEqual(res2, 3)

    def test_mul_area(self):
        res1 = triangle.area(1, 2)
        self.assertEqual(res1, 1)

    def test_mul_perimeter(self):
        res2 = triangle.perimeter(1, 2, 3)
        self.assertEqual(res2, 6)

    def test_big_mul_area(self):
        res1 = triangle.area(1000000, 123456789)
        self.assertEqual(res1, 61728394500000)

    def test_big_mul_perimeter(self):
        res2 = triangle.perimeter(1000000, 23456789, 12345678)
        self.assertEqual(res2, 36802467)
