import unittest

def area(a, b):
    '''
    Принимает стороны прямоугольника a и b, возвращает площадь прямоугольника

    Пример входных данных: 3 5
    Результат: 15
    '''
    return a * b


def perimetr(a, b):
    '''
    Принимает стороны прямоугольника a и b, возвращает периметр прямоугольника

    Пример входных данных: 3 5
    Результат: 16
    '''
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10,0)
        self.assertEqual(res,0)
    
    def test_square_mul(self):
        res = area(10,10)
        self.assertEqual(res,100)

    def test_zero_per(self):
        res = perimetr(10,0)
        self.assertEqual(res,0)

    def test_square_per(self):
        res = perimetr(10,10)
        self.assertEqual(res,40)
