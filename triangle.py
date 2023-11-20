import unittest
import math
def area(a, h):
    '''
    Возвращает площадь треугольника

            Параметры:
                    a (int): сторона треугольника
                    h (int): высота треугольника, ортогональная а.

            Возвращаемое значение:
                    a*h/2 (int): одна вторая произведения a*b

    Пример:

            Входные данные:
                    a = 24
                    h = 8

            Выходные данные:
                    96
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.

            Параметры:
                    a (int): первая сторона треугольника
                    b (int): вторая сторона треугольника
                    c (int): третья сторона треугольника

            Возвращаемое значение:
                    a + b + c (int): сумма a, b и c

    Пример:

            Входные данные:
                    a = 30
                    b = 4
                    c = 15

            Выходные данные:
                    49
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(13.213123, 121.89)
        self.assertEquals(res, 805.273781235)

    def test_one_area(self):
        res = area(math.sqrt(3), math.sqrt(3))
        self.assertEquals(res, 1.5)

    def test_two_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10, 2)
        self.assertEquals(cm.exception.code, 1)

    def test_three_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(1, -20)
        self.assertEquals(cm.exception.code, 1)

    def test_four_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10, -2)
        self.assertEquals(cm.exception.code, 1)

    def test_five_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(10, "vsdv")
        self.assertEquals(cm.exception.code, 1)

    def test_six_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area("faf", 2)
        self.assertEquals(cm.exception.code, 1)

    def test_seven_area(self):
        res = area(0, 10)
        self.assertEquals(res, 0)

    def test_eight_area(self):
        res = area(22, 0)
        self.assertEquals(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(124, 62,9)
        self.assertEquals(res, 195)

    def test_one_perimeter(self):
        res = perimeter(math.sqrt(2), math.sqrt(4),math.sqrt(8))
        self.assertEquals(res, 2 + 3 * math.sqrt(2))

    def test_two_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(41, 1, 2)
        self.assertEquals(cm.exception.code, 1)

    def test_three_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(41, 21, 20)
        self.assertEquals(cm.exception.code, 1)

    def test_four_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(1, -2, 2)
        self.assertNotEquals(cm.exception.code, 1)

    def test_five_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(-1, 2, 2)
        self.assertNotEquals(cm.exception.code, 1)

    def test_six_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(1, 2, -2)
        self.assertNotEquals(cm.exception.code, 1)

    def test_seven_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(1, 2, "-2")
        self.assertNotEquals(cm.exception.code, 1)

    def test_eight_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(1, "sgws", 1)
        self.assertNotEquals(cm.exception.code, 1)

    def test_nine_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(1, 324, "sgws")
        self.assertNotEquals(cm.exception.code, 1)