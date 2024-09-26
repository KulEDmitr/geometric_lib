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

    def test_circle_area_exceptions(self):
        self.assertRaises(ValueError, circle.area, -1)
        self.assertRaises(ValueError, circle.area, -1.23)
        self.assertRaises(TypeError, circle.area, [1])
        self.assertRaises(TypeError, circle.area, '1')
        self.assertRaises(TypeError, circle.area, "abc")

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(10), 62.83185307179586)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.perimeter(1), 6.283185307179586)
        self.assertEqual(circle.perimeter(0.123), 0.7728317927830891)

    def test_circle_perimeter_exceptions(self):
        self.assertRaises(ValueError, circle.perimeter, -1)
        self.assertRaises(ValueError, circle.perimeter, -1.23)
        self.assertRaises(TypeError, circle.perimeter, [1])
        self.assertRaises(TypeError, circle.perimeter, '1')
        self.assertRaises(TypeError, circle.perimeter, "abc")


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(2, 34), 68)
        self.assertEqual(rectangle.area(1, 100), 100)
        self.assertEqual(rectangle.area(0.1, 0.25), 0.025)
        self.assertEqual(rectangle.area(1, 1), 1)
        self.assertEqual(rectangle.area(0, 0), 0)

    def test_rectangle_area_exceptions(self):
        self.assertRaises(ValueError, rectangle.area, -1, -1)
        self.assertRaises(ValueError, rectangle.area, -1.23, -1.23)
        self.assertRaises(TypeError, rectangle.area, [1], [1])
        self.assertRaises(TypeError, rectangle.area, '1', '1')
        self.assertRaises(TypeError, rectangle.area, "abc", "abc")

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 34), 72)
        self.assertEqual(rectangle.perimeter(1, 100), 202)
        self.assertEqual(rectangle.perimeter(0.1, 0.25), 0.7)
        self.assertEqual(rectangle.perimeter(1, 1), 4)
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_rectangle_perimeter_exceptions(self):
        self.assertRaises(ValueError, rectangle.perimeter, -1, -1)
        self.assertRaises(ValueError, rectangle.perimeter, -1.23, -1)
        self.assertRaises(TypeError, rectangle.perimeter, [1], [1])
        self.assertRaises(TypeError, rectangle.perimeter, '1', '1')
        self.assertRaises(TypeError, rectangle.perimeter, "abc", "abc")


class SquareTestCase(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(0.1), 0.01)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(1), 1)

    def test_square_area_exceptions(self):
        self.assertRaises(ValueError, square.area, -1)
        self.assertRaises(ValueError, square.area, -1.23)
        self.assertRaises(TypeError, square.area, [1])
        self.assertRaises(TypeError, square.area, '1')
        self.assertRaises(TypeError, square.area, "abc")

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(0.1), 0.4)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(1), 4)

    def test_square_perimeter_exceptions(self):
        self.assertRaises(ValueError, square.perimeter, -1)
        self.assertRaises(ValueError, square.perimeter, -1.23)
        self.assertRaises(TypeError, square.perimeter, [1])
        self.assertRaises(TypeError, square.perimeter, '1')
        self.assertRaises(TypeError, square.perimeter, "abc")


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle.area(1, 2), 1)
        self.assertEqual(triangle.area(0.01, 2), 0.01)
        self.assertEqual(triangle.area(1, 1), 0.5)
        self.assertEqual(triangle.area(0, 0), 0)

    def test_triangle_area_exceptions(self):
        self.assertRaises(ValueError, triangle.area, -1, -1)
        self.assertRaises(ValueError, triangle.area, -1.23, -1.23)
        self.assertRaises(TypeError, triangle.area, [1], [1])
        self.assertRaises(TypeError, triangle.area, '1', '1')
        self.assertRaises(TypeError, triangle.area, "abc", "abc")

    def test_square_perimeter(self):
        self.assertEqual(triangle.perimeter(1, 2, 3), 6)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(1, 1, 1), 3)
        self.assertEqual(triangle.perimeter(1.2, 2.3, 3.4), 6.9)

    def test_triangle_perimeter_exceptions(self):
        self.assertRaises(ValueError, triangle.perimeter, -1, -1, -1)
        self.assertRaises(ValueError, triangle.perimeter, -1.23, -1.23, -1.23)
        self.assertRaises(TypeError, triangle.perimeter, [1], [1], [1])
        self.assertRaises(TypeError, triangle.perimeter, '1', '1', '1')
        self.assertRaises(TypeError, triangle.perimeter, "abc", "abc", "abc")
