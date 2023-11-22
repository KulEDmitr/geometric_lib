import unittest


def area(a):
    '''
    Возвращает площадь крадрата.
        Параметры:
            a (int): сторона квадрата

        Возвращаемое значение:
            area (int): площадь крадрата со стороной a
    Пример вызова:
        area(2) возвращает 4
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр крадрата.
        Параметры:
            a (int): сторона квадрата

        Возвращаемое значение:
            perimeter (int): периметр крадрата со стороной a
    Пример вызова:
        area(2) возвращает 8
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0)
        res2 = perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)

    def test_mul(self):
        res1 = area(5)
        res2 = perimeter(6)
        self.assertEqual(res1, 25)
        self.assertEqual(res2, 24)

    def test_big_mul(self):
        res1 = area(1000000)
        res2 = perimeter(1000000)
        self.assertEqual(res1, 1000000000000)
        self.assertEqual(res2, 4000000)
