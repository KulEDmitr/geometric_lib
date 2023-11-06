import math
import unittest


def area(r):
    '''
        Функция принимает радиус круга и выводит его площадь

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            area(r) (float): площадь круга, радиуса r

        Пример использования:
            Входные данные
                3.0
            Выходные данные
                28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Функция принимает радиус окружности и выводит её длину

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            perimeter(r) (float): длина окружности радиуса r

        Пример использования:
            Входные данные
                3.0
            Выходные данные
                18.84955592153876
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_regular(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_area_string(self):
        res = area("10")
        self.assertEqual(res, 100 * math.pi)

    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, -10 * math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_regular(self):
        res = perimeter(100)
        self.assertEqual(res, 200 * math.pi)

    def test_perimeter_string(self):
        res = perimeter("100")
        self.assertEqual(res, 200 * math.pi)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertEqual(res, 20 * math.pi)
