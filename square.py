import unittest


def area(a):
    """ 
    Принимает a (сторона квадрата), и возвращает площадь квадрата.
    Пример работы: area(3) - возвращает 9. 
    """
    return a * a


def perimeter(a):
    """ 
    Принимает a (сторона квадрата), и возвращает периметр квадрата.
    Пример работы: perimeter(3) - возвращает 12. 
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_simple_number(self):
        res = area(8)
        self.assertEqual(res, 64)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_large_number(self):
        res = area(12345000)
        self.assertEqual(res, 152399025000000)

    def test_area_negative_number(self):
        res = area(-12345000)
        self.assertEqual(res, 152399025000000)

    def test_perimeter_simple_number(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_large_number(self):
        res = perimeter(12345000)
        self.assertEqual(res, 49380000)

    def test_perimeter_negative_number(self):
        res = perimeter(-12345000)
        self.assertEqual(res, -49380000)
