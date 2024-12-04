import math
import unittest

def area(r):
    '''
    Takes circle radius value, returns circle area value

    Example:
        area(3)
        28.274333882308138
    '''
    if not isinstance(r, int):
        print("Not integer")
        return 0
    if r < 0:
        print("Negative number")
        return 0
    return math.pi * r * r


def perimeter(r):
    '''
    Takes circle radius value, returns circuit value

    Example:
        perimeter(3)
        18.84955592153876
    '''
    if not isinstance(r, int):
        print("Not integer")
        return 0
    if r < 0:
        print("Negative number")
        return 0
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_regular_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_str_area(self):
        res = area("a")
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_regular_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_str_perimeter(self):
        res = perimeter("a")
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, 0)
