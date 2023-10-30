import math
import unittest


def area(r):
    '''
    Возвращает площадь круга по введённому радиусу(формула: S = Pi * r * r)
        Параметры:
            r(float) - радиус круга
        Возвращаемое значение:
            area(r) - площадь круга с радиусом r
        Пример:
            Входные данные: 1.2
            Выходные данные: 4.523893421169302
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга по введённому радиусу(формула: P = Pi * 2 * r)
        Параметры:
            r(float) - радиус круга
        Возвращаемое значение:
            area(r) - периметр круга с радиусом r
        Пример:
            Входные данные: 1.2
            Выходные данные: 7.5398223686155035
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_normal_area(self):
        res = area(10)
        self.assertEqual(res, 314.15926535897932384626433832795)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_normal_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586476925286766559)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
