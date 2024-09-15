import unittest
from triangle import area
from triangle import perimeter


class TriangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        a = area(0, 0)
        self.assertEqual(a, 0)
        a = area(1, 2)
        self.assertEqual(a, 1)
        a = area(10, 5)
        self.assertEqual(a, 25)
        a = area(1, 1)
        self.assertEqual(a, 0.5)

    def test_area_big_numbers(self):
        a = area(10 ** 10, 10 ** 10)
        self.assertEqual(a, 10 ** 20 / 2)
        a = area(1111111111111, 2)
        self.assertEqual(a, 1111111111111)
        a = area(12341234, 12341234)
        self.assertEqual(a, 76153028321378.0)
        a = area(10 ** 100, 10)
        self.assertEqual(a, 10 ** 100 * 5)


class TrianglePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        a = perimeter(0, 0, 0)
        self.assertEqual(a, 0)
        a = perimeter(1, 1, 1)
        self.assertEqual(a, 3)
        a = perimeter(100, 100, 100)
        self.assertEqual(a, 300)
        a = perimeter(13, 12, 11)
        self.assertEqual(a, 36)
        a = perimeter(0.5, 0.5, 1)
        self.assertEqual(a, 2)

    def test_perimeter_big_numbers(self):
        res = perimeter(10 ** 10, 10 ** 10, 10 ** 10)
        self.assertEqual(res, (10 ** 10) * 3)
        res = perimeter(12341234, 12341234, 12341234)
        self.assertEqual(res, 37023702)
        res = perimeter(10 ** 5, 1, 1)
        self.assertEqual(res, 10 ** 5 + 2)
        res = perimeter(11111111111111, 22222222222222, 33333333333333)
        self.assertEqual(res, 66666666666666)
