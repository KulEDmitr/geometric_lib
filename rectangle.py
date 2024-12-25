import unittest

def area(a, b):
    '''Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b.'''
    return a * b 
    
def perimeter(a, b):
    '''Принимает числа a и b, возвращает периметр со сторонами a и b.'''
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
   
    def test_perimeter(self):
        res = perimeter(4, 7)
        self.assertEqual(res, 22)
