import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_perim_13(self):
        res = perimeter(13)
        self.assertEqual(res, math.pi * 26)
    
    def test_perim_1(self):
        res = perimeter(1)
        self.assertEqual(res, math.pi * 2)

    def test_perim_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

def area(r):
    '''Принимает радиус круга, возвращает площадь круга'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает радиус круга, возвращает периметр круга'''
    return 2 * math.pi * r

