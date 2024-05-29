import unittest


def area(a):
    """Пример вызова функции:

    def area(5):
        if 5 == 0:
            return None
        else:
            return 25

    Функция принимает значение стороны квадрата. Если сторона равна 0, то квадрата не существет, иначе функция возвращает его площадь.
    """
    if a == 0:
        return None
    else:
        return a * a


def perimeter(a):
    """Пример вызова функции:

    def perimeter(5):
        if 5 == 0:
            return None
        else:
            return 20

    Функция принимает значение стороны квадрата. Если сторона равна 0, то квадрата не существет, иначе функция возвращает его периметр.
    """
    if a == 0:
        return None
    else:
        return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(area(0), None)
        self.assertEqual(perimeter(0), None)

    def test_value_mul(self):
        self.assertEqual(area(3), 9)
        self.assertEqual(perimeter(3), 12)
