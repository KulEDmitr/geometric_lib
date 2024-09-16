# import unittest

def area(a, b):
    '''
    Параметры: a - длина прямоугольникаб, b - ширина прямоугольника
    Возвращает площадь прямоугольника
    area(a, b): площадь прямоугольника со сторонами a и b
    '''

    return a * b

def perimeter(a, b):
    '''
    Параметры: a - длина прямоугольникаб, b - ширина прямоугольника
    Возвращает периметр прямоугольника
    perimeter(a, b): периметр прямоугольника со сторонами a и b
    '''
    return 2 * (a + b)


# class RectangleTestCase(unittest.TestCase):
#     def test_zero_mul(self):
#         res = area(10, 0)
#         self.assertEqual(res, 0)
#
#     def test_square_mul(self):
#         res = area(10, 10)
#         self.assertEqual(res, 100)
