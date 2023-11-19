import unittest


def area(a, b):
    """
    Принимает величину сторон прямоугольника и возвращает его площадь	
    Пример вызова:
    area(2, 3)
    Возвращаемое значение:
    6
    """
    return a * b


def perimeter(a, b):
    """
    Принимает величину сторон прямоугольника и возвращает его периметр	
    Пример вызова:
    perimeter(2, 3)
    Возвращаемое значение:
    10
    """
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(1, 2)
        self.assertEqual(res, 1 * 2, "Fail test number 1, area(1, 2)")

    def test_area_2(self):
        res = area(-1, 2)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1, 2)")

    def test_area_3(self):
        self.assertRaises(TypeError, area, "a", 2, "Fail test number 3, area(a, 2)")

    def test_area_4(self):
        res = area(4, 5)
        self.assertEqual(res, 5 * 4, "Fail test number 4, area(4, 5)")

    def test_area_5(self):
        res = area(10000000000000000000000000000, 10000000000000000000000000000)
        self.assertEqual(res, (10000000000000000000000000000 ** 2), "Fail test number 5, area("
                                                                    "10000000000000000000000000000, "
                                                                    "10000000000000000000000000000)")

    def test_perimetr_1(self):
        res = perimeter(1, 2)
        self.assertEqual(res, (1 + 2) * 2, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        res = perimeter(-1, 1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, perimetr(-1, 1)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, perimeter, "a", "b", "Fail test number 3, perimetr(a, b)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, perimeter, 1, "Fail test number 3, perimetr(1)")

    def test_perimetr_5(self):
        res = perimeter(10000000000000000000000000000, 10000000000000000000000000000)
        self.assertEqual(res, (10000000000000000000000000000 + 10000000000000000000000000000) * 2,
                         "Fail test number 5, perimetr(10000000000000000000000000000, 10000000000000000000000000000)")
