from unittest import TestCase

def area(a, b):
    '''Возвращает площадь прямоугольника со сторонами a и b
        Параметры:
            a, b: стороны прямоугольника
        Возвращаемое значение:
            a * b: площадь прямоугольника
        Пример вызова area(3, 2):
            Входные данные: 3 2
            Вывод: 6'''

    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0 or b <= 0:
        raise ValueError("Argument must be positive")

    return a * b

def perimeter(a, b):
    '''Возвращает периметр прямоугольника со сторонами a и b
        Параметры:
            a, b: стороны прямоугольника
        Возвращаемое значение:
            (a + b) * 2: периметр прямоугольника
        Пример вызова perimetr(3, 2)`:
            Входные данные: 3 2
            Вывод: 10'''

    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0 or b <= 0:
        raise ValueError("Argument must be positive")

    return (a + b) * 2

class RectangleTestCase(TestCase):
    def test_area_with_integer_dimensions(self):
        self.assertEqual(area(3, 4), 12)

    def test_area_with_float_dimensions(self):
        self.assertEqual(area(2.5, 1.5), 3.75)

    def test_area_with_mixed_types(self):
        self.assertEqual(area(2, 2.0), 4.0)

    def test_area_with_incorrect_type(self):
        self.assertRaises(TypeError, area, [], 1)

    def test_area_with_negative_value(self):
        self.assertRaises(ValueError, area, 2, -3)

    def test_area_with_zero_value(self):
        self.assertRaises(ValueError, area, 0, 1)

    def test_perimeter_with_integer_dimensions(self):
        self.assertEqual(perimeter(3, 4), 14)

    def test_perimeter_with_float_dimensions(self):
        self.assertEqual(perimeter(2.5, 1.5), 8.0)

    def test_perimeter_with_mixed_types(self):
        self.assertEqual(perimeter(2.0, 3), 10)

    def test_perimeter_with_incorrect_type(self):
        self.assertRaises(TypeError, perimeter, [], [])

    def test_perimeter_with_negative_value(self):
        self.assertRaises(ValueError, perimeter, -2, 3)

    def test_perimeter_with_zero_value(self):
        self.assertRaises(ValueError, perimeter, 1, 0)