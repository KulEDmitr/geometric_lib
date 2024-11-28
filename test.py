import unittest
from circle import CircleArea, CirclePerimeter
from rectangle import RectangleArea, RectanglePerimeter
from square import SquareArea, SquarePerimeter
from triangle import TriangleArea, TrianglePerimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_natural_numbers(self):
        res = TriangleArea(10, 15)
        self.assertEqual(res, 75.0)

    # def test_triangle_area_negative_numbers(self):
    #     res = TriangleArea(-10, -3)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_triangle_area_chars(self):
    #     res = TriangleArea(-10, "a")
    #     self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_triangle_area_big_numbers(self):
        res = TriangleArea(9000000000, 1000000000)
        self.assertEqual(res, 4500000000000000000)

    def test_triangle_perimeter_natural_numbers(self):
        res = TrianglePerimeter(9, 12, 15)
        self.assertEqual(res, 36)

    # def test_triangle_perimeter_negative_number(self):
    #     res = TrianglePerimeter(-10, 10, -10)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_triangle_perimeter_chars(self):
    #     res = TrianglePerimeter(3, "a", "b")
    #     self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_triangle_perimeter_big_numbers(self):
        res = TrianglePerimeter(9000000, 10000000, 10000000)
        self.assertEqual(res, 29000000)

class SquareTestCase(unittest.TestCase):
    def test_square_area_natural_numbers(self):
        res = SquareArea(100)
        self.assertEqual(res, 10000)

    # def test_square_area_negative_number(self):
    #     res = SquareArea(-10)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_square_area_chars(self):
    #     res = SquareArea("a")
    #     self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_square_area_big_numbers(self):
        res = SquareArea(90000000000)
        self.assertEqual(res, 8100000000000000000000)

    def test_square_perimeter_natural_numbers(self):
        res = SquarePerimeter(10)
        self.assertEqual(res, 40)

    # def test_square_perimeter_negative_number(self):
    #     res = SquarePerimeter(-10)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_square_perimeter_chars(self):
    #     res = SquarePerimeter("a")
    #     self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_square_perimeter_big_numbers(self):
        res = SquarePerimeter(90000000000)
        self.assertEqual(res, 360000000000)


class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_natural_numbers(self):
        res = RectangleArea(300, 200)
        self.assertEqual(res, 60000)

    # def test_rectangle_area_negative_number(self):
    #     res = RectangleArea(-100, 40)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_rectangle_area_chars(self):
    #     res = RectangleArea("a", "b")
    #     self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_rectangle_area_big_numbers(self):
        res = RectangleArea(9000000000, 8000000000)
        self.assertEqual(res, 72000000000000000000)

    def test_rectangle_perimeter_natural_numbers(self):
        res = RectanglePerimeter(10, 40)
        self.assertEqual(res, 100)

    # def test_rectangle_perimeter_negative_number(self):
    #     res = RectanglePerimeter(-10, 0)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_rectangle_perimeter_chars(self):
    #     res = RectanglePerimeter("a", 0)
    #     self.assertEqual(res, "Incorrect input! Input values should be numbers")

    def test_rectangle_perimeter_big_numbers(self):
        res = RectanglePerimeter(9000000000, 7000000000)
        self.assertEqual(res, 32000000000)

class CircleTestCase(unittest.TestCase):
    def test_circle_area_natural_numbers(self):
        res = CircleArea(10)
        self.assertEqual(res, 314.1592653589793)

    def test_circle_area_big_numbers(self):
        res = CircleArea(9000000000)
        self.assertEqual(res, 2.5446900494077326e+20)

    # def test_circle_area_negative_number(self):
    #     res = CircleArea(-10)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_circle_area_chars(self):
    #     res = CircleArea("a")
    #     self.assertEqual(res, "Incorrect input! Input value should be number")

    def test_circle_perimeter_natural_numbers(self):
        res = CirclePerimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_circle_perimeter_big_numbers(self):
        res = CirclePerimeter(90000000000)
        self.assertEqual(res, 565486677646.1627)

    # def test_circle_perimeter_negative_number(self):
    #     res = CirclePerimeter(-10)
    #     self.assertEqual(res, "Incorrect input! Input numbers should be positive")
    #
    # def test_circle_perimeter_chars(self):
    #     res = CirclePerimeter("a")
    #     self.assertEqual(res, "Incorrect input! Input value should be number")
