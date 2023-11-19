import math
import unittest


def area(r):
    """
    Принимает радиус окружности и возвращает её площадь	   
    Пример вызова:
    area(2)
    Возвращаемое значение:
    12.56...
    """
    return math.pi * r * r


def perimeter(r):
    """
    Принимает радиус окружности и возвращает её периметр	
    Пример вызова:
    perimeter(2)
    Возвращаемое значение:
    12.56...
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, math.pi * (1 ** 2), "Fail test number 1, area(1)")

    def test_area_2(self):
        res = area(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1)")

    def test_area_3(self):
        self.assertRaises(TypeError, area, "a", "Fail test number 3, area(a)")

    def test_area_4(self):
        res = area(4)
        self.assertEqual(res, math.pi * (4 ** 2), "Fail test number 4, area(4)")

    def test_area_5(self):
        res = area(10000000000000000000000000000)
        self.assertEqual(res, math.pi * (10000000000000000000000000000 ** 2), "Fail test number 5, area("
                                                                              "10000000000000000000000000000)")

    def test_perimetr_1(self):
        res = perimeter(1)
        self.assertEqual(res, 2 * math.pi * 1, "Fail test number 1, perimetr(1)")

    def test_perimetr_2(self):
        res = perimeter(-1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, perimetr(-1)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, perimeter, "a", "Fail test number 3, perimetr(a)")

    def test_perimetr_4(self):
        res = perimeter(4)
        self.assertEqual(res, math.pi * 2 * 4, "Fail test number 4, perimetr(4)")

    def test_perimetr_5(self):
        res = perimeter(10000000000000000000000000000)
        self.assertEqual(res, math.pi * 10000000000000000000000000000 * 2,
                         "Fail test number 5, perimetr(10000000000000000000000000000)")
        print(res)
