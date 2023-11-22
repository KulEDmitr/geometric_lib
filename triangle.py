import unittest


def area(a, h):
    '''
    Возвращает площадь треугольника.
        Параметры:
            a (int): сторона треугольника
            h (int): высота треугольника

        Возвращаемое значение:
            area (int): площадь треугольника со стороной a и высотой h
    Пример вызова:
        area(1, 2) возвращает 1
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.
        Параметры:
            a (int): сторона треугольника
            b (int): сторона треугольника
            c (int): сторона треугольника

        Возвращаемое значение:
            perimeter (int): периметр треугольника со сторонами a, b и с
    Пример вызова:
        area(1, 2, 3) возвращает 6
    '''
    return a + b + c


print(perimeter(1000000, 23456789, 12345678))


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0, 56)
        res2 = perimeter(0, 1, 2)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 3)

    def test_mul(self):
        res1 = area(1, 2)
        res2 = perimeter(1, 2, 3)
        self.assertEqual(res1, 1)
        self.assertEqual(res2, 6)

    def test_big_mul(self):
        res1 = area(1000000, 123456789)
        res2 = perimeter(1000000, 23456789, 12345678)
        self.assertEqual(res1, 61728394500000)
        self.assertEqual(res2, 36802467)
