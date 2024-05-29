import unittest


def area(a, b):
    """Пример вызова функции:

    def area(4, 3):
        if (4 == 0 or 3 == 0)
            return None
        else:
            return 12

    Функция принимает значения двух сторон прямоугольника. Если одна из сторон равна 0, то прямоугольника не существует, иначе функция возвращает его площадь.
    """
    if a == 0 or b == 0:
        return None
    else:
        return a * b


def perimeter(a, b):
    """Пример вызова функции:

    def perimeter(4, 3):
        if 4 == 0 or 3 == 0:
            return None
        else:
            return 14

    Функция принимает значения двух сторон прямоугольника. Если одна из сторон равна 0, то прямоугольника не существует, иначе функция функция возвращает его периметр.
    """
    if a == 0 or b == 0:
        return None
    else:
        return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertIsNone(area(4, 0), None)
        self.assertIsNone(perimeter(0, 5), None)

    def test_value_mul(self):
        self.assertEqual(area(4, 3), 12)
        self.assertEqual(perimeter(4, 3), 14)
