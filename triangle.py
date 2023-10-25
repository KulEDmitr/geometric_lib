import unittest


def area(a, h):
    '''
        Функция принимает сторону треугольника и его высоту, выводит его площадь

        Параметры:
            a (float): сторона треугольника
            h (float): высота треугольника

        Возвращаемое значение:
            area(a, b) (float): площадь треугольника со стороной a и высотой b

        Пример использования:
            Входные данные
                2.0  3.0
            Выходные данные
                3.0
    '''
    return a * h / 2 


def perimeter(a, b, c):
    '''
        Функция принимает стороны треугольника и выводит его периметр

        Параметры:
            a (float): первая сторона треугольника
            b (float): вторая сторона треугольника
            с (float): третья сторона треугольника

        Возвращаемое значение:
            perimeter(a, b, c) (float): периметр треугольника со сторонами a, b и c

        Пример использования:
            Входные данные
                2.0  3.0  4.0
            Выходные данные
                9.0
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_perimeter_1(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_2(self):
        res = perimeter(101, 101, 101)
        self.assertEqual(res, 303)
