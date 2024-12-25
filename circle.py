import math
import unittest

def area(r):
    '''Принимает число r, возвращает площадь окружности с радиусом r.'''
    return math.pi * r * r

def perimeter(r):
    '''Принимает число r, возвращает периметр окружности с радиусом r.'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_one(self):
       res = area(6)
       self.assertEqual(res, 113.09733552923255)
       
    def test_two(self):
       res = perimeter(6)
       self.assertEqual(res, 37.69911184307752)
       
    def test_three(self):
       res = area(4)
       self.assertEqual(res, 50.26548245743669)
       
    def test_four(self):
       res = perimeter(4)
       self.assertEqual(res, 25.132741228718345)