import math
import unittest


def area(r):
    '''
    Возвращает площадь круга.
        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            area (int): площадь круга радиусом r
    Пример вызова:
        area(1) возвращает 3,14
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.
        Параметры:
            r (int): радиус круга

        Возвращаемое значение:
            perimeter (int): периметр круга радиусом r
    Пример вызова:
        perimeter(1) возвращает 6,28
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        res1 = area(0)
        self.assertEqual(res1, 0)

    def test_zero_mul_perimeter(self):
        res2 = perimeter(0)
        self.assertEqual(res2, 0)

    def test_mul_area(self):
        res1 = area(10)
        self.assertEqual(res1, 314.1592653589793)

    def test_mul_perimeter(self):
        res2 = perimeter(10)
        self.assertEqual(res2, 62.83185307179586)

    def test_big_mul_area(self):
        res1 = area(1000000)
        self.assertEqual(res1, 3141592653589.793)

    def test_big_mul_perimeter(self):
        res2 = perimeter(1000000)
        self.assertEqual(res2, 6283185.307179586)
