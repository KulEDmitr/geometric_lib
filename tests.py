import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle.area(10), 314.1592653589793)
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.area(1), 3.141592653589793)
        self.assertEqual(circle.area(0.123), 0.04752915525615998)
        self.assertEqual(circle.area(5), 78.53981633974483)

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(10), 62.83185307179586)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.perimeter(1), 6.283185307179586)
        self.assertEqual(circle.perimeter(0.123), 0.7728317927830891)
        self.assertEqual(circle.perimeter(5), 31.41592653589793)


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(2, 34), 68)
        self.assertEqual(rectangle.area(1, 100), 100)
        self.assertEqual(rectangle.area(0.1, 0.25), 0.025)
        self.assertEqual(rectangle.area(0.0001, 10), 0.001)
        self.assertEqual(rectangle.area(1, 1000000), 1000000)
        self.assertEqual(rectangle.area(1, 1), 1)
        self.assertEqual(rectangle.area(0, 0), 0)
        self.assertEqual(rectangle.area(10, 0), 0)
        self.assertEqual(rectangle.area(0, 10), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 34), 72)
        self.assertEqual(rectangle.perimeter(1, 100), 202)
        self.assertEqual(rectangle.perimeter(0.1, 0.25), 0.7)
        self.assertEqual(rectangle.perimeter(0.0001, 10), 20.0002)
        self.assertEqual(rectangle.perimeter(1, 1000000), 2000002)
        self.assertEqual(rectangle.perimeter(8, 8), 32)
        self.assertEqual(rectangle.perimeter(1, 1), 4)
        self.assertEqual(rectangle.perimeter(0, 0), 0)


class SquareTestCase(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(1), 1)

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(10), 40)
        self.assertEqual(square.perimeter(0.1), 0.4)
        self.assertEqual(square.perimeter(0.0001), 0.0004)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(1), 4)


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle.area(1, 2), 1)
        self.assertEqual(triangle.area(3, 4), 6)
        self.assertEqual(triangle.area(8, 8), 32)
        self.assertEqual(triangle.area(10, 8), 40)
        self.assertEqual(triangle.area(2, 80), 80)
        self.assertEqual(triangle.area(10, 20), 100)
        self.assertEqual(triangle.area(0.0001, 2), 0.0001)
        self.assertEqual(triangle.area(1, 1), 0.5)
        self.assertEqual(triangle.area(0, 1), 0)
        self.assertEqual(triangle.area(1, 0), 0)
        self.assertEqual(triangle.area(0, 0), 0)

    def test_square_perimeter(self):
        self.assertEqual(triangle.perimeter(1203, 123, 12312), 13638)
        self.assertEqual(triangle.perimeter(1, 2, 3), 6)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)
        self.assertEqual(triangle.perimeter(4, 4, 5), 13)
        self.assertEqual(triangle.perimeter(1.2, 2.3, 3.4), 6.9)
