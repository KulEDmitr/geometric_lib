import unittest


def area(a, h):
    """Пример вызова функции:

    def area(7, 6):
        if a == 0 or h == 0:
            return None
        else:
            return 21

    Функция принимает значения стороны и высоты треугольника к этой стороне. Если сторона или высота треугольника равны 0, то треугольника не существует, иначе функция возвращает его площадь.
    """
    if a == 0 or h == 0:
        return None
    else:
        return a * h / 2


def perimeter(a, b, c):
    """Пример вызова функции:

    def perimeter(6, 5, 4):
        if 6 != 0 and 5 != 0 and 4 != 0:
            if 6 + 5 > 4 and 6 + 4 > 5 and 5 + 4 > 6:
                return 15
        else:
            return None

    Функция принимает значения трех сторон треугольника. Если хоть одна сторона равна 0, то треугольника не существет, если сумма двух любых сторон меньше третьей, то треугольника не существует, иначе функция возвращает его периметр.
    """
    if a != 0 and b != 0 and c != 0:
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
    else:
        return None


class TrinagleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertIsNone(area(7, 0), None)
        self.assertIsNone(perimeter(1, 3, 0), None)

    def test_value_mul(self):
        self.assertEqual(area(7, 6), 21)
        self.assertIsNone(perimeter(1, 2, 3), None)
