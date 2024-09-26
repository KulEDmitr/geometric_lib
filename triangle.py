import unittest


def area(a, h):
    """
    Принимает длину основания треугольника a и его высоту h и возвращает его площадь.

    Пример:
        Ввод:
        a = 3
        h = 4

        Вывод:
        6.0
    :param a: Длина основания.
    :param h: Высота.
    :return: Площадь.
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Принимает длины сторон треугольника a, b и c и возвращает его периметр.

    Пример:
        Ввод:
        a = 3
        b = 4
        c = 5

        Вывод:
        12
    :param a: Длина стороны a.
    :param b: Длина стороны b.
    :param c: Длина стороны c.
    :return: Периметр.
    """
    return a + b + c


class TriangleTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 6.0)
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(area(-3, 4), -6.0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(0, 4, 5), 9)
        self.assertEqual(perimeter(-3, 4, 5), 6)
