import math
import unittest

#вызывает библиотеку math

def area(r):
    '''
        принимает цулое число r ,предполагаемый радиус окружности
        возвращает значение площади с плавающей точкой
        r(5) = pi * 5 * 5 = 78,5398
    '''
    return math.pi * r * r

def perimeter(r):
    '''
        принимает целое r ,предполагаемый радиус окружности
        возвращает значение периметра с плавающей точкой
        r(5) = 2 * pi * r = 31,4159265359
    '''
    return 2 * math.pi * r
class CIRCLETEST(unittest.TestCase):
    def test_int(self):
        n = int(input("введите число для вычисления круга(целое и неотрицательное):"))
        if(n > 0 and n < 10**9):
            x = True
        else:
            x = False
        self.assertTrue(x)
    def test_c_area_const(self):
        result = circle.area(5)
        self.assertEqual(result, 78.53981633974483)

    def test_c_perimeter_const(self):
        result2 = circle.perimeter(5)
        self.assertEqual(result2, 31.41592653589793)
