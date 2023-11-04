import unittest


def area(a, b):
    '''
        Функция принимает стороны прямоугольника и выводит его площадь

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            area(a, b) (float): площадь прямоугольника со сторонами a и b

        Пример использования:
            Входные данные
                2.0  3.0
            Выходные данные
                6.0
    '''
    return a * b


def perimeter(a, b):
    '''
        Функция принимает стороны прямоугольника и выводит его периметр

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            perimeter(a, b) (float): периметр прямоугольника со сторонами a и b

        Пример использования:
            Входные данные
                2.0  3.0
            Выходные данные
                10.0
    '''
    return a + b + a + b


class RectangleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_negative(self):
        res = area(-10, 10)
        self.assertEqual(res, 100)

    def test_perimeter_1(self):
        res = perimeter(0, 10)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(100, 10)
        self.assertEqual(res, 220)

    def test_perimeter_negative(self):
        res = perimeter(-100, 10)
        self.assertEqual(res, 220)