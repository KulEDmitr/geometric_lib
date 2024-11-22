import unittest

def area(a):
    '''
    Принимает сторону квадрата a, возвращает площадь квадрата

    Пример входных данных: 3
    Результат: 9
    '''
    return a * a


def perimetr(a):
    '''
    Принимает сторону квадрата a, возвращает периметр квадрата

    Пример входных данных: 3
    Результат: 12
    '''
    return 4 * a

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res,0)
    
    def test_def_area(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_zero_per(self):
        res = perimetr(0)
        self.assertEqual(res,0)

    def test_def_per(self):
        res = perimetr(3)
        self.assertEqual(res,12)