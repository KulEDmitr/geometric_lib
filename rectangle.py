import unittest

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_mul(self):
        res = area(0, 1)
        self.assertEqual(res, "IllegalArgumentException")
    def test_rectangle_int_mul(self):
        res = area(5, 6)
        self.assertEqual(res, 30)
    def test_rectangle_float_mul(self):
        res = area(2.39, 2.23)
        self.assertEqual(res, 5.3297)
    def test_rectangle_negative_mul(self):
        res = area(-1, -1)
        self.assertEqual(res, "IllegalArgumentException")
    def test_rectangle_one_string_mul(self):
        res = area('1', 5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_rectangle_two_strings_mul(self):
        res = area('1', '2')
        self.assertEqual(res, "IllegalArgumentException")
    def test_rectangle_zero_perimeter(self):
        res = perimeter(0, 1)
        self.assertEqual(res, "IllegalArgumentException")
    def test_rectangle_int_perimeter(self):
        res = perimeter(5, 6)
        self.assertEqual(res, 22)
    def test_rectangle_float_perimeter(self):
        res = perimeter(2.39, 2.23)
        self.assertEqual(res, 9.24)
    def test_rectangle_negative_perimeter(self):
        res = perimeter(-5, 7)
        self.assertFalse(res, "IllegalArgumentException")
    def test_rectangle_one_string_perimeter(self):
        res = perimeter('23', 9)
        self.assertFalse(res, "IllegalArgumentException")
    def test_rectangle_two_strings_perimeter(self):
        res = perimeter('23', '9')
        self.assertFalse(res, "IllegalArgumentException")

def area(a, b):
    '''
    Возвращает площадь прямоугольника с заданными сторонами.

            Параметры:
                    a (float): первая сторона прямоугольника
                    b (float): вторая сторона прямоугольника

            Возвращаемое значение:
                    rectangle_area (float): площадь прямоугольника со сторонами a и b

    Примеры вызова функции:
        area(5.0, 6.0) = 30.0
        area(2.39, 2.23) = 5.3297
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника с заданными сторонами.

            Параметры:
                    a (float): первая сторона прямоугольника
                    b (float): вторая сторона прямоугольника

            Возвращаемое значение:
                    rectangle_perimeter (float): периметр прямоугольника со сторонами a и b

    Примеры вызова функции:
        perimeter(5.0, 6.0) = 22.0
        perimeter(2.39, 2.23) = 9.24
    '''
    return 2*(a + b)
