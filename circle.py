import unittest
import math


def area(r):
    '''
    Takes the radius of a circle and returns its area
    Example:
    print(area(5)) // 78.53981633974483
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Takes the radius of a circle and returns its perimeter
    Example:
    print(perimeter(5)) // 31.41592653589793
    '''
    return 2 * math.pi * r

class SquareTestCase(unittest.TestCase):
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = area(10)
        self.assertEqual(res, 314.15926535897932384626433832795)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5")