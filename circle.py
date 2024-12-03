import math
import unittest
import math

def area(r):
    return math.pi * r * r
    '''
       Вычисляет площадь круга.

       Параметры:
       r (float): Радиус окружности.

       Возвращаемое значение:
       float: Площадь круга.

       Исключения: Отсутствуют.  

       Пример:
       >>> area(10)
       314,1529
    '''

def perimeter(r):
    return 2 * math.pi * r
    '''
       Вычисляет длину окружности.

       Параметры:
       r (float): Радиус окружности.

       Возвращаемое значение:
       float: Длина окружности.

       Исключения: Отсутствуют.  

       Пример:
       >>> perimeter(10)
       62,8318
    '''


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(2)
        self.assertEqual(res, math.pi * 2 * 2)

    def test_perimeter(self):
        res = area(2)
        self.assertEqual(res, 2 * math.pi * 2)
