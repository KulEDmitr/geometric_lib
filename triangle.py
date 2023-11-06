import unittest
def area(a, h):
    '''
    Возвращает площадь треугольника по введёным значениям основания и высоты(формуле S = a * h)
        Параметры:
            a(float) - длина основания
            h(float) - высота треугольника
        Возвращаемое значение:
            area(a, h) - высота треугольника с основанием a и высотой h
        Пример:
            Входные данные: 1.1 2.0
            Выходные данные: 1.1
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника по введённым значениям трёх сторон(формула: P = a + b + c)
        Параметры:
            a(float) - первая сторона
            b(float) - вторая сторона
            c(float) - третья сторона
        Возвращаемое значение:
            perimeter(a, b, c) - периметр треугольника со сторонами a, b, c
        Пример:
            Входные данные: 1.1 2.0 3.0
            Выходные данные: 6.1
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_normal_perimeter(self):
        res = perimeter(10, 20, 30)
        self.assertEqual(res, 60)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-10, 10)
        self.assertEqual(res, 50)

    def test_negative_perimeter(self):
        res = perimeter(-10, 20, 30)
        self.assertEqual(res, 60)

    def test_huge_perimeter(self):
        res = perimeter(12738495757192482917, 1, 1)
        self.assertEqual(res, 12738495757192482919)

    def test_huge_area(self):
        res = area(878545256984,  439272628492)
        self.assertEqual(res, 192960442142270650194064)

    def test_unparsable_area(self):
        res = area("10u81h", "5xlerghlzi")
        self.assertEqual(res, 25)

    def test_unparsable_perimeter(self):
        res = perimeter("10nfk34ngi", "20fsdflui4585", "30esilgb485")
        self.assertEqual(res, 60)

    def test_double_area(self):
        res = area(0.1, 0.2)
        self.assertEqual(res, 0.01)

    def test_double_perimeter(self):
        res = perimeter(0.1, 0.2, 0.3)
        self.assertEqual(res, 0.6)
