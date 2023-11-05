import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_circle_zero_mul(self):
        res = area(0)
        self.assertEqual(res, "IllegalArgumentException")
    def test_circle_int_mul(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)
    def test_circle_float_mul(self):
        res = area(2.39)
        self.assertEqual(res, 17.94509139657026)
    def test_circle_negative_mul(self):
        res = area(-3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_circle_string_mul(self):
        res = area('3')
        self.assertEqual(res, "IllegalArgumentException")
    def test_circle_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, "IllegalArgumentException")
    def test_circle_int_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)
    def test_circle_float_perimeter(self):
        res = perimeter(2.39)
        self.assertEqual(res, 15.016812884159211)
    def test_circle_negative_perimeter(self):
        res = perimeter(-3.14)
        self.assertEqual(res, "IllegalArgumentException")
    def test_circle_string_perimeter(self):
        res = perimeter('3')
        self.assertEqual(res, "IllegalArgumentException")


def area(r):
    '''
    Возвращает площадь круга с заданным радиусом.

            Параметры:
                    r (float): радиус круга

            Возвращаемое значение:
                    circle_area (float): площадь круга с радиусом r

    Примеры вызова функции:
        area(3.0) = 28.274333882308138
        area(2.39) = 17.94509139657026
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с заданным радиусом.

            Параметры:
                    r (float): радиус круга

            Возвращаемое значение:
                    circle_perimeter (float): периметр круга с радиусом r

    Примеры вызова функции:
        perimeter(3.0) = 18.84955592153876
        perimeter(2.39) = 15.016812884159211
    '''
    return 2 * math.pi * r

