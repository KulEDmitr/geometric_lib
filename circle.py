import math
import unittest

def area(r):
    '''
    принимает радиус круга r, возвращает площадь круга
    
    пример входных данных: 4
    результат: 50.26548245743669
    '''
    return math.pi * r * r


def perimetr(r):
    '''
    принимает радиус круга r, возвращает периметр круга
    
    пример выходных данных: 4
    результат: 25.132741228718345
    '''
    return 2 * math.pi * r

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area('a')
        self.assertEqual(res,0)
    
    def test_def_area(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_zero_per(self):
        res = perimetr(0)
        self.assertEqual(res,0)

    def test_def_per(self):
        res = perimetr(4)
        self.assertEqual(res,25.132741228718345)
