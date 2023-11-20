import math
import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника.

            Параметры:
                    a (int): первая сторона прямоугольника
                    b (int): вторая сторона прямоугольника

            Возвращаемое значение:
                    a*b (int): произведение a и b
    Пример:

            Входные данные:
                    a = 30
                    b = 4

            Выходные данные:
                    120
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

            Параметры:
                    a (int): первая сторона прямоугольника
                    b (int): вторая сторона прямоугольника

            Возвращаемое значение:
                    2*(a + b) (int): удвоенная сумма a и b в виде десятичного целого числа

    Пример:

            Входные данные:
                    a = 30
                    b = 4

            Выходные данные:
                    68
    '''
    return 2*(a + b)

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 23)
        self.assertEquals(res, 0)

    def test_one_area(self):
        res = area(35, 0)
        self.assertEquals(res, 0)

    def test_two_area(self):
        res = area(1.0/math.sqrt(math.pi), 1.0/math.sqrt(math.pi))
        self.assertEquals(res, 1/math.pi)

    def test_three_area(self):
        res = area(7, 21)
        self.assertEquals(res, 147)

    def test_four_area(self):
        res = area(0.125, 5)
        self.assertEquals(res, 0.625)

    def test_five_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10, 43)
        self.assertEquals(cm.exception.code, 1)

    def test_six_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(10, -43)
        self.assertEquals(cm.exception.code, 1)

    def test_seven_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area("vsdv", 432)
        self.assertEquals(cm.exception.code, 1)

    def test_eight_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(21, "vsdv")
        self.assertEquals(cm.exception.code, 1)

    def test_zero_perimeter(self):
        res = perimeter(0, 23)
        self.assertEquals(res, 46)

    def test_one_perimeter(self):
        res = perimeter(35, 0)
        self.assertEquals(res, 70)

    def test_two_perimeter(self):
        res = perimeter(math.sqrt(math.pi), math.sqrt(math.pi))
        self.assertEquals(res, 4 * math.sqrt(math.pi))

    def test_three_perimeter(self):
        res = perimeter(7, 21)
        self.assertEquals(res, 56)

    def test_four_perimeter(self):
        res = perimeter(0.125, 5)
        self.assertEquals(res, 10.25)

    def test_five_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(-10, 43)
        self.assertEquals(cm.exception.code, 1)

    def test_six_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(10, -43)
        self.assertEquals(cm.exception.code, 1)

    def test_seven_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter("vsdv", 432)
        self.assertEquals(cm.exception.code, 1)

    def test_eight_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(21, "vsdv")
        self.assertEquals(cm.exception.code, 1)