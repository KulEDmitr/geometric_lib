import math
from unittest import TestCase

def area(r):
    '''Возвращает площадь круга с радиусом r.
            Параметры:
                    r (int): радиус круга
            Возвращаемое значение:
                    pi * r * r (float): площадь круга с радиусом r
            Пример вызова area(3):
                    Входные данные: 3
                    Вывод: 28.2743338823'''

    if not (isinstance(r, int) or isinstance(r, float)):
        raise TypeError("Argument must be int or float")

    if r <= 0:
        raise ValueError("Argument must be positive")

    return math.pi * r * r


def perimeter(r):
    '''Возвращает периметр круга с радиусом r.
            Параметры:
                    r (int): радиус круга
            Возвращаемое значение:
                    2 * pi * r (float): периметр круга с радиусом r
            Пример вызова perimetr(3):
                    Входные данные: 3
                    Вывод: 18.8495559215'''

    if not (isinstance(r, int) or isinstance(r, float)):
        raise TypeError("Argument must be int or float")

    if r <= 0:
        raise ValueError("Argument must be positive")

    return 2 * math.pi * r




class CircleTestCase(TestCase):
    def test_area_with_integer_radius(self):
        self.assertEqual(area(5), 78.53981633974483)

    def test_area_with_float_radius(self):
        self.assertEqual(area(2.5), 19.634954084936208)

    def test_area_with_incorrect_type_radius(self):
        self.assertRaises(TypeError, area, [])

    def test_area_with_negative_radius(self):
        self.assertRaises(ValueError, area, -1)

    def test_area_with_zero_radius(self):
        self.assertRaises(ValueError, area, 0)

    def test_perimeter_with_integer_radius(self):
        self.assertEqual(perimeter(4), 25.132741228718345)

    def test_perimeter_with_float_radius(self):
        self.assertEqual(perimeter(3.5), 21.991148575128552)

    def test_perimeter_with_incorrect_type_radius(self):
        self.assertRaises(TypeError, perimeter, [])

    def test_perimeter_with_negative_radius(self):
        self.assertRaises(ValueError, perimeter, -2)

    def test_perimeter_with_zero_radius(self):
        self.assertRaises(ValueError, perimeter, 0)