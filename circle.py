import math
import unittest
class TestRectangleMethods(unittest.TestCase):
    def tests_normal_data(self):
        self.assertAlmostEqual(area(1), 3.14159265)
        self.assertAlmostEqual(area(3), 28.27433388)
        self.assertAlmostEqual(perimeter(1), 6.2831853)
        self.assertAlmostEqual(perimeter(3), 18.8495559)


    def test_zeros(self):
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            perimeter(0)


    def test_neg_numbers(self):
        with self.assertRaises(ValueError):
            area(-1)
        with self.assertRaises(ValueError):
            perimeter(-5)


    def test_wrong_types(self):
        with self.assertRaises(TypeError):
            area("ab") 
        with self.assertRaises(TypeError):
            area("33")
        with self.assertRaises(TypeError):
            perimeter("ab")
        with self.assertRaises(TypeError):
            perimeter("33")


def area(r):
    '''
    Accepts number r - radius of circle,
    returns area of a circle of given radius.
        Example: area(3) -> 28.2743338823
    '''

    return math.pi * r * r


def perimeter(r):
    '''
    Accepts number r - the radius of the circle,
    returns the length of the circle of radius r.
        Example: perimeter(3) -> 18.8495559215
    '''

    return 2 * math.pi * r
