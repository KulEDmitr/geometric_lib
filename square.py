import unittest


def area(a):
    """
    Принимает длину стороны квадрата a и возвращает его площадь.

    Пример:
        Ввод:
        a = 5

        Вывод:
        25
    :param a: Длина стороны a.
    :return: Площадь.
    """
    return a * a


def perimeter(a):
    """
    Принимает длину стороны квадрата a и возвращает его периметр.

    Пример:
        Ввод:
        a = 5

        Вывод:
        20
    :param a: Длина стороны a.
    :return: Периметр.
    """
    return 4 * a


class SquareTests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(-5), 25)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(-5), -20)
