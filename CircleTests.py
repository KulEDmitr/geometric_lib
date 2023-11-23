import math
import unittest
from circle import area
from circle import perimeter


class CircleAreaTestCase(unittest.TestCase):
    def test_area(self):
        a = area(0)
        self.assertEqual(a, 0)
        a = area(2)
        self.assertEqual(a, math.pi * 4)
        a = area(5)
        self.assertEqual(a, math.pi * 25)
        a = area(0.5)
        self.assertEqual(a, math.pi * 0.25)

    def test_area_big_numbers(self):
        a = area(10 ** 10)
        self.assertEqual(a, math.pi * 10 ** 20)
        a = area(111111111111)
        self.assertEqual(a, math.pi * 12345679012320987654321)
        a = area(12341234)
        self.assertEqual(a, math.pi * 152306056642756)
        a = area(12341234123412341234)
        self.assertEqual(a, math.pi * 152306059688877178543891480857256642756)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_perimeter(self):
        a = perimeter(0)
        self.assertEqual(a, 0)
        a = perimeter(1)
        self.assertEqual(a, 2 * math.pi)
        a = perimeter(100)
        self.assertEqual(a, math.pi * 200)
        a = perimeter(13)
        self.assertEqual(a, math.pi * 26)
        a = perimeter(0.3)
        self.assertEqual(a, math.pi * 0.6)

    def test_perimeter_big_numbers(self):
        res = perimeter(10 ** 10)
        self.assertEqual(res, 2 * math.pi * (10 ** 10))
        res = perimeter(12341234)
        self.assertEqual(res, math.pi * 24682468)
        res = perimeter(11 ** 5)
        self.assertEqual(res, math.pi * 11 ** 5 * 2)
        res = perimeter(33333333333333)
        self.assertEqual(res, math.pi * 33333333333333)
