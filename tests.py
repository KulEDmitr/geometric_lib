import unittest
import circle
import rectangle
import triangle
import square
import math

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(circle.area(3), math.pi * 3 * 3)
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.area(1563215215), math.pi * 1563215215 * 1563215215)
        self.assertEqual(circle.area(0.005), math.pi * 0.005 * 0.005)
        self.assertEqual(circle.area(3.973628), math.pi * 3.973628 * 3.973628)

    def test_circle_area_value(self):
        self.assertRaises(ValueError, circle.area, -2)
        self.assertRaises(ValueError, circle.area, -4.8734)
        self.assertRaises(ValueError, circle.area, "a")
        self.assertRaises(ValueError, circle.area, "3")
        self.assertRaises(ValueError, circle.area, [2])

    def test_circle_perimeter(self):
        self.assertEqual(circle.perimeter(5), 2 * math.pi * 5)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.perimeter(1563215215), 2 * math.pi * 1563215215)
        self.assertEqual(circle.perimeter(0.006), 2 * math.pi * 0.006)
        self.assertEqual(circle.perimeter(4.56), 2 * math.pi * 4.56)

    def test_circle_perimeter_value(self):
        self.assertRaises(ValueError, circle.perimeter, -10)
        self.assertRaises(ValueError, circle.perimeter, -4.8734)
        self.assertRaises(ValueError, circle.perimeter, "b")
        self.assertRaises(ValueError, circle.perimeter, "4")
        self.assertRaises(ValueError, circle.perimeter, [19])


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        self.assertEqual(rectangle.area(3, 5), 15)
        self.assertEqual(rectangle.area(0, 7), 0)
        self.assertEqual(rectangle.area(2.5, 4), 10)
        self.assertEqual(rectangle.area(1000, 0.005), 5)
        self.assertEqual(rectangle.area(4.0, 2.0), 8.0)
        self.assertEqual(rectangle.area(6.2, 0.3), 1.86)

    def test_rectangle_area_value(self):
        self.assertRaises(ValueError, rectangle.area, -2, 5)
        self.assertRaises(ValueError, rectangle.area, -4.8734, 2.0)
        self.assertRaises(ValueError, rectangle.area, -4.8, -2.7)
        self.assertRaises(ValueError, rectangle.area, "a", 4)
        self.assertRaises(ValueError, rectangle.area, 3, "a")
        self.assertRaises(ValueError, rectangle.area, "5", "2")
        self.assertRaises(ValueError, rectangle.area, [2], 9)
        self.assertRaises(ValueError, rectangle.area, 3, [4])
        self.assertRaises(ValueError, rectangle.area, [2], [3])

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle.perimeter(5, 3), 16)
        self.assertEqual(rectangle.perimeter(0, 7), 0)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        self.assertEqual(rectangle.perimeter(0.2, 0.3), 1)
        self.assertEqual(rectangle.perimeter(2.5, 4.5), 14.0)

    def test_rectangle_perimeter_value(self):
        self.assertRaises(ValueError, rectangle.perimeter, -10, 2)
        self.assertRaises(ValueError, rectangle.perimeter, -4.8, 4.0)
        self.assertRaises(ValueError, rectangle.perimeter, -8, -4)
        self.assertRaises(ValueError, rectangle.perimeter, -3.0, -4.0)
        self.assertRaises(ValueError, rectangle.perimeter, "b", 2)
        self.assertRaises(ValueError, rectangle.perimeter, 12, "4")
        self.assertRaises(ValueError, rectangle.perimeter, 3.8, "2.9")
        self.assertRaises(ValueError, rectangle.perimeter, "3", "5")
        self.assertRaises(ValueError, rectangle.perimeter, [5], 4)
        self.assertRaises(ValueError, rectangle.perimeter, [19], [23])


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle.area(3, 6), 9)
        self.assertEqual(triangle.area(3, 5), 7.5)
        self.assertEqual(triangle.area(0, 7), 0)
        self.assertEqual(triangle.area(2.5, 4), 5.0)
        self.assertEqual(triangle.area(4.0, 2.0), 4.0)
        self.assertEqual(triangle.area(6.2, 0.3), 0.93)

    def test_triangle_area_value(self):
        self.assertRaises(ValueError, triangle.area, -2, 5)
        self.assertRaises(ValueError, triangle.area, -4.8734, 2.0)
        self.assertRaises(ValueError, triangle.area, -4.8, -2.7)
        self.assertRaises(ValueError, triangle.area, "a", 4)
        self.assertRaises(ValueError, triangle.area, 5, "a")
        self.assertRaises(ValueError, triangle.area, "5", "2")
        self.assertRaises(ValueError, triangle.area, [2], 9)
        self.assertRaises(ValueError, triangle.area, 3, [4])
        self.assertRaises(ValueError, triangle.area, [2], [3])

    def test_triangle_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 3, 7), 15)
        self.assertEqual(triangle.perimeter(0, 7, 4), 0)
        self.assertEqual(triangle.perimeter(0, 0, 3), 0)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        self.assertEqual(triangle.perimeter(0.2, 0.3, 2), 2.5)
        self.assertEqual(triangle.perimeter(2.5, 4.5, 3.7), 10.7)

    def test_triangle_perimeter_value(self):
        self.assertRaises(ValueError, triangle.perimeter, 2, 3, 9)
        self.assertRaises(ValueError, triangle.perimeter, -10, 2, 4)
        self.assertRaises(ValueError, triangle.perimeter, 4.8, -4.0, 9)
        self.assertRaises(ValueError, triangle.perimeter, 5, -8, -4)
        self.assertRaises(ValueError, triangle.perimeter, -3.0, -4.0, -5.0)
        self.assertRaises(ValueError, triangle.perimeter, "4", 3, 2)
        self.assertRaises(ValueError, triangle.perimeter, 2, "3", "4")
        self.assertRaises(ValueError, triangle.perimeter, 3.8, "2.9", 6)
        self.assertRaises(ValueError, triangle.perimeter, "3", "5", "4")
        self.assertRaises(ValueError, triangle.perimeter, [5], 4, 7)
        self.assertRaises(ValueError, triangle.perimeter, [19], [23], [17])


class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square.area(3), 9)
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area(2.5), 6.25)
        self.assertEqual(square.area(10.0), 100.0)

    def test_square_area_value(self):
        self.assertRaises(ValueError, square.area, -2)
        self.assertRaises(ValueError, square.area, -4.8)
        self.assertRaises(ValueError, square.area, "a")
        self.assertRaises(ValueError, square.area, "5")
        self.assertRaises(ValueError, square.area, [2])

    def test_square_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter(0.2), 0.8)

    def test_square_perimeter_value(self):
        self.assertRaises(ValueError, square.perimeter, -10)
        self.assertRaises(ValueError, square.perimeter, -4.8)
        self.assertRaises(ValueError, square.perimeter, "b")
        self.assertRaises(ValueError, square.perimeter, "4")
        self.assertRaises(ValueError, square.perimeter, [5])


if __name__ == '__main__':
    unittest.main()