import math
import unittest

import Rectangle
import circle
import triangle
import square

class SquareTestCase(unittest.TestCase):

    def test_perimetr_1(self):
        res = Rectangle.perimeter(1)
        self.assertEqual(res, 4 * 1, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        self.assertRaises(TypeError, square.perimeter, 1, 1, "Fail test number 2, perimetr(1, 1)")

    def test_perimetr_3(self):
        res = square.perimeter(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 3, perimetr(-1)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, square.perimeter, "a", "Fail test number 4, perimetr(a)")

    def test_perimetr_5(self):
        res = square.perimeter(100000000000000000000000000000000000000000)
        self.assertEqual(res, 4 * 100000000000000000000000000000000000000000,
                         "Fail test number 5, perimetr(100000000000000000000000000000000000000000)")

    def test_area_1(self):
        res = square.area(1)
        self.assertEqual(res, 1 * 1)

    def test_area_2(self):
        self.assertRaises(TypeError, square.area, 1, 2, "Fail test number 2, perimetr(1, 2)")

    def test_area_3(self):
        res = square.area(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 3, area(-1)")

    def test_area_4(self):
        self.assertRaises(TypeError, square.area, "a", "Fail test number 4, area(a)")

    def test_area_5(self):
        res = square.area(10000000000000000000000000000000000000000)
        self.assertEqual(res, 10000000000000000000000000000000000000000 * 10000000000000000000000000000000000000000,
                         "Fail test number 5, area(100000000000000000000000000000000000000000)")

class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = Rectangle.area(1, 2)
        self.assertEqual(res, 1 * 2, "Fail test number 1, area(1, 2)")

    def test_area_2(self):
        res = Rectangle.area(-1, 2)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1, 2)")

    def test_area_3(self):
        self.assertRaises(TypeError, Rectangle.area("a", 2), "Fail test number 3, area(a, 2)")

    def test_area_4(self):
        res = Rectangle.area(4, 5)
        self.assertEqual(res, 5 * 4, "Fail test number 4, area(4, 5)")

    def test_area_5(self):
        res = Rectangle.area(10000000000000000000000000000, 10000000000000000000000000000)
        self.assertEqual(res, (10000000000000000000000000000 ** 2), "Fail test number 5, area("
                                                                    "10000000000000000000000000000, "
                                                                    "10000000000000000000000000000)")

    def test_perimetr_1(self):
        res = Rectangle.perimeter(1, 2)
        self.assertEqual(res, (1 + 2) * 2, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        res = Rectangle.perimeter(-1, 1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, perimetr(-1, 1)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, Rectangle.perimeter, "a", "b", "Fail test number 3, perimetr(a, b)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, Rectangle.perimeter, 1, "Fail test number 3, perimetr(1)")

    def test_perimetr_5(self):
        res = Rectangle.perimeter(10000000000000000000000000000, 10000000000000000000000000000)
        self.assertEqual(res, (10000000000000000000000000000 + 10000000000000000000000000000) * 2,
                         "Fail test number 5, perimetr(10000000000000000000000000000, 10000000000000000000000000000)")


class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi * (1 ** 2), "Fail test number 1, area(1)")

    def test_area_2(self):
        res = circle.area(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1)")

    def test_area_3(self):
        self.assertRaises(TypeError, circle.area, "a", "Fail test number 3, area(a)")

    def test_area_4(self):
        res = circle.area(4)
        self.assertEqual(res, math.pi * (4 ** 2), "Fail test number 4, area(4)")

    def test_area_5(self):
        res = circle.area(10000000000000000000000000000)
        self.assertEqual(res, math.pi * (10000000000000000000000000000 ** 2), "Fail test number 5, area("
                                                                              "10000000000000000000000000000)")

    def test_perimetr_1(self):
        res = circle.perimeter(1)
        self.assertEqual(res, 2 * math.pi * 1, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        res = circle.perimeter(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, perimetr(-1)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, circle.perimeter, "a", "Fail test number 3, perimetr(a)")

    def test_perimetr_4(self):
        res = circle.perimeter(4)
        self.assertEqual(res, math.pi * 2 * 4, "Fail test number 4, perimetr(4)")

    def test_perimetr_5(self):
        res = circle.perimeter(10000000000000000000000000000)
        self.assertEqual(res, math.pi * 10000000000000000000000000000 * 2,
                         "Fail test number 5, perimetr(10000000000000000000000000000)")
        print(res)

class TriangleTestCase(unittest.TestCase):

    def test_perimetr_1(self):
        res = triangle.perimeter(2, 2, 3)
        self.assertEqual(res, 2 + 2 + 3)

    def test_perimetr_2(self):
        res = triangle.area(-1, 2, -3)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1, 2, -3)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, triangle.perimeter, 1, 2, 3, 4,  "Fail test number 3, perimetr(1, 2, 3, 4)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, triangle.perimeter, 1, 2, "a",  "Fail test number 4, perimetr(1, 2, a)")

    def test_perimetr_5(self):
        res = triangle.perimeter(1000000000000, 4, 4)
        self.assertEqual(res, -1, "Fail test number 5, perimetr(1000000000000, 4, 4)")

    def test_area_1(self):
        res = triangle.area(1, 2, 2)
        half_per = (1 + 2 + 2) / 2
        self.assertEqual(res, (half_per * (half_per - 1) * (half_per - 2) * (half_per - 2)) ** 0.5,
                         "Fail test number 1, area(1, 2, 2)")

    def test_area_2(self):

        
        res = triangle.area(2, 4, -1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(2, 4, -1)")

    def test_area_3(self):
        self.assertRaises(TypeError, triangle.perimeter, 1, 2, 3, 4,  "Fail test number 3, area(1, 2, 3, 4)")

    def test_area_4(self):
        self.assertRaises(TypeError, triangle.perimeter, 1, 2, "a",  "Fail test number 4, area(1, 2, a)")

    def test_area_5(self):
        res = triangle.area(1000000000000, 4, 4)
        self.assertEqual(res, -1, "Fail test number 5, area(1000000000000, 4, 4)")
