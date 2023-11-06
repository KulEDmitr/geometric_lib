import unittest


def area(a):
    '''
    Возвращает площадь квадрата по введённой стороне(формула: S = a * a)
        Параметры:
            a(float) - сторона квадрата
        Возвращаемое значение:
            area(a) - площадь квадрата со стороной a
        Пример:
            Входные данные: 1.2
            Выходные данные: 1.44
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата по введённой стороне(формула: P = 4 * a)
        Параметры:
            a(float) - сторона квадрата
        Возвращаемое значение:
            perimeter(a) - периметр квадрата со стороной a
        Пример:
            Входные данные: 1.2
            Выходные данные: 4.8
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-10)
        self.assertEqual(res, 100)

    def test_negative_perimeter(self):
        res = perimeter(-10)
        self.assertEqual(res, 40)

    def test_area_normal(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_normal_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_huge_perimeter(self):
        res = perimeter(12738495757192482917)
        self.assertEqual(res, 50953983028769931668)

    def test_huge_area(self):
        res = area(878545256984)
        self.assertEqual(res, 771841768569082600776256)

    def test_unparsable_area(self):
        res = area("10u81h")
        self.assertEqual(res, 100)

    def test_unparsable_perimeter(self):
        res = perimeter("10nfk34ngi")
        self.assertEqual(res, 40)

    def test_double_area(self):
        res = area(0.1)
        self.assertEqual(res, 0.01)

    def test_double_perimeter(self):
        res = perimeter(0.1)
        self.assertEqual(res, 0.4)
