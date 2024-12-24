from unittest import TestCase

def area(a, h):
    '''
    Возвращает площадь треугольника со стороной a и высотой h
                Параметры:
                    a: сторона треугольника
                    h: высота треугольника
                Возвращаемое значение:
                    a * a: площадь треугольника
                Пример вызова area(3, 2):
                    Входные данные: 3, 2
                    Вывод: 3
                    '''

    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(h, int) or isinstance(h, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0 or h <= 0:
        raise ValueError("Argument must be positive")

    return a * h / 2
    

def perimeter(a, b, c):
    '''Возвращает периметр треугольника со сторонами a, b и c 
        Параметры:
            a, b, c: стороны треугольника
            h: высота треугольника
        Возвращаемое значение:
            a + b + c: периметр треугольника
        Пример вызова perimetr(3, 2, 1):
            Входные данные: 3 2 1
            Вывод: 6'''

    if not (isinstance(a, int) or isinstance(a, float)) or not (isinstance(b, int) or isinstance(b, float)) or not (isinstance(c, int) or isinstance(c, float)):
        raise TypeError("Argument must be int or float")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Argument must be positive")

    return a + b + c

class TriangleTestCase(TestCase):
    def test_area_with_integer_base_and_height(self):
        self.assertEqual(area(2, 3), 3)

    def test_area_with_float_base_and_height(self):
        self.assertEqual(area(1.5, 4.0), 3.0)

    def test_area_with_mixed_types(self):
        self.assertEqual(area(1.5, 4), 3.0)

    def test_area_with_invalid_type(self):
        self.assertRaises(TypeError, area, [], [])

    def test_area_with_negative_base(self):
        self.assertRaises(ValueError, area, -3, 2)

    def test_area_with_zero_height(self):
        self.assertRaises(ValueError, area, 1, 0)

    def test_perimeter_with_integer_sides(self):
        self.assertEqual(perimeter(1, 2, 3), 6)

    def test_perimeter_with_float_sides(self):
        self.assertEqual(perimeter(1.5, 1.0, 2.5), 5.0)

    def test_perimeter_with_mixed_types(self):
        self.assertEqual(perimeter(1.5, 1, 2.5), 5.0)

    def test_perimeter_with_invalid_type(self):
        self.assertRaises(TypeError, perimeter, [], [], [])

    def test_perimeter_with_negative_side(self):
        self.assertRaises(ValueError, perimeter, -3, 2, 1)

    def test_perimeter_with_zero_side(self):
        self.assertRaises(ValueError, perimeter, 0, 3, 2)