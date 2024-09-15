import unittest
from rectangle import area
from rectangle import perimeter


class RectangleAreaTestCase(unittest.TestCase):
    def test_area(self):
        a = area(0, 0)
        self.assertEqual(a, 0)
        a = area(1, 1)
        self.assertEqual(a, 1)
        a = area(10, 5)
        self.assertEqual(a, 50)
        a = area(1, 0.5)
        self.assertEqual(a, 0.5)

    def test_area_big_numbers(self):
        a = area(10 ** 10, 10 ** 10 + 1)
        self.assertEqual(a, 10 ** 20 + 1)
        a = area(111111111111, 2)
        self.assertEqual(a, 222222222222)
        a = area(12341234, 12341234)
        self.assertEqual(a, 152306056642756)
        a = area(10 ** 100, 10)
        self.assertEqual(a, 10 ** 101)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        a = perimeter(0, 0)
        self.assertEqual(a, 0)
        a = perimeter(1, 1)
        self.assertEqual(a, 4)
        a = perimeter(100, 100)
        self.assertEqual(a, 400)
        a = perimeter(13, 12)
        self.assertEqual(a, 50)
        a = perimeter(0.5, 1)
        self.assertEqual(a, 3)

    def test_perimeter_big_numbers(self):
        res = perimeter(10 ** 10, 10 ** 10)
        self.assertEqual(res, (10 ** 10) * 4)
        res = perimeter(12341234, 12341234)
        self.assertEqual(res, 49364936)
        res = perimeter(10 ** 5, 1)
        self.assertEqual(res, (10 ** 5 + 1) * 2)
        res = perimeter(11111111111111, 22222222222222)
        self.assertEqual(res, 33333333333333)
