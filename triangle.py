import unittest

def area(a, h): 
    '''
    Принимает сторону треугольника a и высоту треугольника h, возвращает площадь треугольника

    Пример входных данных: 4 5
    Результат: 10
    '''
    return a * h / 2 

def perimetr(a, b, c): 
    '''
    Принимает стороны треугольника a, b, c , возвращает площадь треугольника

    Пример входных данных: 3 4 5
    Результат: 12
    '''
    return a + b + c

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 2)
        self.assertEqual(res,0)
    
    def test_def_area(self):
        res = area(4, 5)
        self.assertEqual(res, 10)

    def test_zero_per(self):
        res = perimetr(0, 3 ,5)
        self.assertEqual(res,0)

    def test_def_per(self):
        res = perimetr(3, 4, 5)
        self.assertEqual(res, 12)