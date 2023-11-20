import math
import unittest

def area(r):
    '''
    Возвращает площадь круга

            Параметры:
                    r (int): радиус круга

            Возвращаемое значение:
                    pi*r*r (int): произведение квадрата a и числа пи

    Пример:

            Входные данные:
                    r = 4

            Выходные данные:
                    50.26548245743669
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга

            Параметры:
                    r (int): радиус круга

            Возвращаемое значение:
                    2*r*pi (int): произведение 2, a и числа пи

    Пример:

            Входные данные:
                    r = 7

            Выходные данные:
                    43.98229715025711
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEquals(res, 0.0)

    def test_one_area(self):
        res = area(1.0/math.sqrt(math.pi))
        self.assertEquals(res, 1.0)

    def test_two_area(self):
        res = area(7)
        self.assertEquals(res, 153.93804002589985)

    def test_three_area(self):
        res = area(0.324)
        self.assertEquals(res, 0.3297918304032421)

    def test_four_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10)
        self.assertEquals(cm.exception.code, 1)

    def test_five_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area("vsdv")
        self.assertEquals(cm.exception.code, 1)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEquals(res, 0.0)

    def test_one_perimeter(self):
        res = perimeter(1/(2*math.pi))
        self.assertEquals(res, 1.0)

    def test_two_perimeter(self):
        res = perimeter(0.5)
        self.assertEquals(res, 3.141592653589793)

    def test_three_perimeter(self):
        res = perimeter(7)
        self.assertEquals(res, 43.982297150257104)

    def test_four_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10)
        self.assertEquals(cm.exception.code, 1)

    def test_five_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = area("vsdv")
        self.assertEquals(cm.exception.code, 1)