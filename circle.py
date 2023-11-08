import unittest
import math


def area(r):
    ''' Принимает число r на вход, возвращает pi * r*r - площадь круга '''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r на вход, возвращает 2*pi*r - периметр круга '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_area_2(self):
        res = area(2)
        self.assertEqual(res, 4*math.pi)

    def test_perimeter_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(17.5)
        self.assertEqual(res, 35*math.pi)

    def test_perimeter_2(self):
        res = perimeter(17.23)
        self.assertEqual(res, 34.46 * math.pi)

    def test_perimeter(self):
        self.assertEqual(perimeter(-1), -2*math.pi)