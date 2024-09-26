import unittest


def area(a):
    '''
        Функция принимает сторону квадрата и выводит его площадь

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            area(a) (float): площадь квадрата со стороной a

        Пример использования:
            Входные данные
                3.0
            Выходные данные
                9.0
    '''
    return a * a


def perimeter(a):
    '''
        Функция принимает сторону квадрата и выводит его периметр

        Параметры:
            a (float): сторона квадрата

        Возвращаемое значение:
            perimeter(a) (float): периметр квадрата со стороной a

        Пример использования:
            Входные данные
                3.0
            Выходные данные
                12.0
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, -1)

    def test_area_regular(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_string(self):
        res = area("10")
        self.assertEqual(res, -1)

    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, -1)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, -1)

    def test_perimeter_regular(self):
        res = perimeter(101)
        self.assertEqual(res, 404)

    def test_perimeter_string(self):
        res = perimeter("101")
        self.assertEqual(res, -1)

    def test_perimeter_negative(self):
        res = perimeter(-101)
        self.assertEqual(res, -1)
