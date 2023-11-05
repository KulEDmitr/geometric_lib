import unittest

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_mul(self):
        res = area(0, 1)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_int_mul(self):
        res = area(23, 9)
        self.assertEqual(res, 103.5)
    def test_triangle_float_mul(self):
        res = area(5.5, 7.6)
        self.assertEqual(res, 20.9)
    def test_triangle_negative_mul(self):
        res = area(-1, -1)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_one_string_mul(self):
        res = area('1', 2)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_two_strings_mul(self):
        res = area('1', '2')
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_zero_perimeter(self):
        res = perimeter(0, 5, 6)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_int_perimeter(self):
        res = perimeter(23, 9, 17)
        self.assertEqual(res, 49)
    def test_triangle_float_perimeter(self):
        res = perimeter(5.5, 9.6, 7.6)
        self.assertEqual(res, 22.7)
    def test_triangle_neq_perimeter(self):
        res = perimeter(5.5, 6.6, 77.7)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_negative_perimeter(self):
        res = perimeter(-5.5, -6.6, 7.7)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_one_string_perimeter(self):
        res = perimeter('3', 4, 5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_triangle_three_strings_perimeter(self):
        res = perimeter('3', '4', '5')
        self.assertEqual(res, "IllegalArgumentException")

def area(a, h):
    '''
    Возвращает площадь треугольника с заданной стороной и высотой, опущенной на данную сторону.

            Параметры:
                    a (float): заданная сторона треугольника
                    h (float): высота, опущенная на данную сторону треугольника

            Возвращаемое значение:
                    triangle_area (float): площадь треугольника со стороной a и высотой h, опущенной на сторону a

    Примеры вызова функции:
        area(23.0, 9.0) = 103.5
        area(5.5, 7.6) = 20.9
    '''
    return a*h/2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника с заданными сторонами.

            Параметры:
                    a (float): первая сторона треугольника
                    b (float): вторая сторона треугольника
                    c (float): третья сторона треугольника

            Возвращаемое значение:
                    triangle_perimeter (float): площадь треугольника со сторонами a, b и c

    Примеры вызова функции:
        perimeter(23.0, 9.0, 17.0) = 49.0
        perimeter(5.5, 9.6, 7.6) = 22.7
    '''
    return a+b+c
