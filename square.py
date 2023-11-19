import unittest


def area(a):
    """
    Принимает величину стороны квадрата и возвращает его площадь
    Пример вызова:
    area(2)
    Возвращаемое значение:
    4
    """
    return a * a


def perimeter(a):
    """
    Принимает величину стороны квадрата и возвращает его периметр
    Пример вызова:
    perimeter(2)
    Возвращаемое значение:
    8
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):

    def test_perimetr_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4 * 1, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        self.assertRaises(TypeError, perimeter, 1, 1, "Fail test number 2, perimetr(1, 1)")

    def test_perimetr_3(self):
        res = perimeter(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 3, perimetr(-1)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, perimeter, "a", "Fail test number 4, perimetr(a)")

    def test_perimetr_5(self):
        res = perimeter(100000000000000000000000000000000000000000)
        self.assertEqual(res, 4 * 100000000000000000000000000000000000000000,
                         "Fail test number 5, perimetr(100000000000000000000000000000000000000000)")

    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, 1 * 1)

    def test_area_2(self):
        self.assertRaises(TypeError, area, 1, 2, "Fail test number 2, perimetr(1, 2)")

    def test_area_3(self):
        res = area(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 3, area(-1)")

    def test_area_4(self):
        self.assertRaises(TypeError, area, "a", "Fail test number 4, area(a)")

    def test_area_5(self):
        res = area(10000000000000000000000000000000000000000)
        self.assertEqual(res, 10000000000000000000000000000000000000000 * 10000000000000000000000000000000000000000,
                         "Fail test number 5, area(100000000000000000000000000000000000000000)")