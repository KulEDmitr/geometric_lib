import unittest

def area(a, h):
    '''Принимает числа a и h, возвращает площадь треугольника со стороной a и высотой h.'''
    return a * h / 2 
 
def perimeter(a, b, c):
    '''Принимает числа a и h, возвращает периметр треугольника со сторонами a, b и c.'''
    return a + b + c 

class CircleTestCase(unittest.TestCase):
   def test_one(self):
       res = area(7, 2)
       self.assertEqual(res, 7.0)
       
   def test_two(self):
       res = perimeter(9, 14, 6)
       self.assertEqual(res, 29)