import unittest
def area(a, b):
    '''
    Возвращает площадь прямоугольника по введённым сторонам(формула: S = a * b)
        Параметры:
            a(float) - первая сторона прямоугольника
            b(float) - вторая сторона прямоугольника
        Возвращаемое значение:
            area(a, b) - площадь прямоугольника со сторонами a, b
        Пример:
            Входные данные: 1.2 2.0
            Выходные данные: 2.4
    '''
    return a * b 

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника по введённым сторонам(формула: P = 2 * (a + b))
        Параметры:
            a(float) - первая сторона прямоугольника
            b(float) - вторая сторона прямоугольника
        Возвращаемое значение:
            perimeter(a, b) - периметр прямоугольника со сторонами a, b
        Пример:
            Входные данные: 1.2 2.0
            Выходные данные: 6.4
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_normal_area(self):
        res = area(10, 2)
        self.assertEqual(res, 20)

    def test_normal_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-10, 10)
        self.assertEqual(res, 100)

    def test_negative_perimeter(self):
        res = perimeter(-10, 2)
        self.assertEqual(res, 24)

    def test_huge_perimeter(self):
        res = perimeter(12738495757192482917, 12738495757192482918)
        self.assertEqual(res, 50953983028769931670)

    def test_huge_area(self):
        res = area(878545256984, 878545256983)
        self.assertEqual(res, 771841768568204055519272)

    def test_unparsable_area(self):
        res = area("10u81h", "20fesh4")
        self.assertEqual(res, 200)

    def test_unparsable_perimeter(self):
        res = perimeter("10nfk34ngi", "20soigh3")
        self.assertEqual(res, 60)

    def test_double_area(self):
        res = area(0.1, 0.2)
        self.assertEqual(res, 0.02)

    def test_double_perimeter(self):
        res = perimeter(0.1, 0.2)
        self.assertEqual(res, 0.6)
