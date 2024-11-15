import unittest

def area(a):
    '''Принимает число a, возвращает площадь квадрата со сторонами a.'''
    return a * a
    
def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со сторонами a.'''
    return 4 * a

class CircleTestCase(unittest.TestCase):
   def test_one(self):
       res = area(72)
       self.assertEqual(res, 5184)
       
   def test_two(self):
       res = perimeter(23)
       self.assertEqual(res, 92)