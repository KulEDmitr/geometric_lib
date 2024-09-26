import unittest


def area(a, b):
    """
    Принимает длины сторон прямоугольника a и b и возвращает его площадь.

    Пример:
        Ввод:
        a = 3
        b = 4

        Вывод:
        12
    :param a: Длина стороны a.
    :param b: Длина стороны b.
    :return: Площадь.
    """
    return a * b


def perimeter(a, b):
    """
    Принимает длины сторон прямоугольника a и b и возвращает его периметр.

    Пример:
        Ввод:
        a = 3
        b = 4

        Вывод:
        14
    :param a: Длина стороны a.
    :param b: Длина стороны b.
    :return: Периметр.
    """
    return (a + b) * 2


class RectangleTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 12)
        self.assertEqual(area(0, 4), 0)
        self.assertEqual(area(-3, 4), -12)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), 14)
        self.assertEqual(perimeter(0, 4), 8)
        self.assertEqual(perimeter(-3, 4), 2)
