import unittest
import math

def area(a):
    '''
    Возвращает площадь квадрата

            Параметры:
                    a (int): сторона квадрата

            Возвращаемое значение:
                    a*a (int): квадрат a

    Пример:

            Входные данные:
                    a = 4

            Выходные данные:
                    16
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата

             Параметры:
                    a (int): сторона квадрата

            Возвращаемое значение:
                    4*a (int): произведение 4 и a

    Пример:

            Входные данные:
                    a = 24

            Выходные данные:
                    96
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(13.213123)
        self.assertEquals(res, 174.586619413129)

    def test_one_area(self):
        res = area(21)
        self.assertEquals(res, 441)

    def test_two_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area(-10)
        self.assertEquals(cm.exception.code, 1)

    def test_three_area(self):
        with self.assertRaises(SystemExit) as cm:
            res = area("vsdv")
        self.assertEquals(cm.exception.code, 1)

    def test_four_area(self):
        res = area(0)
        self.assertEquals(res, 0)

    def test_five_area(self):
        res = area(1 + math.sqrt(2))
        self.assertEquals(res, 3 + 2 * math.sqrt(2))

    def test_zero_perimeter(self):
        res = perimeter(62)
        self.assertEquals(res, 248)

    def test_one_perimeter(self):
        res = perimeter(0.3333333333333333333333)
        self.assertEquals(res, 1.3333333333333333333332)

    def test_two_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter(-41)
        self.assertEquals(cm.exception.code, 1)

    def test_three_perimeter(self):
        with self.assertRaises(SystemExit) as cm:
            res = perimeter("-2")
        self.assertNotEquals(cm.exception.code, 1)

    def test_four_perimeter(self):
        res = perimeter(math.sqrt(2))
        self.assertEquals(res, 4 * math.sqrt(2))

    def test_five_perimeter(self):
        res = area(0)
        self.assertEquals(res, 0)