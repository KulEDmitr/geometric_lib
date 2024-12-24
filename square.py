from unittest import TestCase

def area(a):
    '''Возвращает площадь квадрата со стороной a
        Параметры:
            a: сторона квадрата
        Возвращаемое значение:
            a * a: площадь квадрата
        Пример вызова area(3):
            Входные данные: 3
            Вывод: 9'''

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0:
        raise ValueError("Argument must be positive")

    return a * a


def perimeter(a):
    '''Возвращает периметр квадрата со стороной a
        Параметры:
            a: сторона квадрата
        Возвращаемое значение:
            a * 4: периметр квадрата
        Пример вызова perimetr(3):
            Входные данные: 3
            Вывод: 12'''

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0:
        raise ValueError("Argument must be positive")

    return 4 * a

class SquareTestCase(TestCase):
    def test_area_with_integer_dimension(self):
        self.assertEqual(area(3), 9)

    def test_area_with_float_dimension(self):
        self.assertEqual(area(2.5), 6.25)

    def test_area_with_incorrect_type(self):
        self.assertRaises(TypeError, area, [])

    def test_area_with_negative_value(self):
        self.assertRaises(ValueError, area, -1)

    def test_area_with_zero_value(self):
        self.assertRaises(ValueError, area, 0)

    def test_perimeter_with_integer_dimension(self):
        self.assertEqual(perimeter(3), 12)

    def test_perimeter_with_float_dimension(self):
        self.assertEqual(perimeter(2.5), 10.0)

    def test_perimeter_with_incorrect_type(self):
        self.assertRaises(TypeError, perimeter, [])

    def test_perimeter_with_negative_value(self):
        self.assertRaises(ValueError, perimeter, -1)

    def test_perimeter_with_zero_value(self):
        self.assertRaises(ValueError, perimeter, 0)
