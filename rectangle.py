import unittest


def area(a, b):
    '''
    Возвращает площадь прямоугольника.
        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника

        Возвращаемое значение:
            area (int): площадь прямоугольника со сторонами a и b
    Пример вызова:
        area(1, 2) возвращает 2
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.
        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника

        Возвращаемое значение:
            perimeter (int): периметр прямоугольника со сторонами a и b
    Пример вызова:
        area(1, 2) возвращает 6
    '''
    return 2 * (a + b)


print(perimeter(1000000, 20000023))


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res1 = area(0, 5)
        res2 = perimeter(0, 7)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 14)

    def test_mul(self):
        res1 = area(2, 5)
        res2 = perimeter(2, 8)
        self.assertEqual(res1, 10)
        self.assertEqual(res2, 20)

    def test_big_mul(self):
        res1 = area(1000000, 2000000)
        res2 = perimeter(1000000, 20000023)
        self.assertEqual(res1, 2000000000000)
        self.assertEqual(res2, 42000046)
