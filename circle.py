import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, math.pi * 20)

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

