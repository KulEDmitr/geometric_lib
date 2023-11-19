import unittest


def existing(a, b, c):
    """
    Принимает переменные a, b и c, стороны треугольника
    И возвращает true если треугольник существует
    false в обратном случае
    Пример вызова:
    existing(1, 1, 1)
    Возвращаемое значение:
    true
    """
    if a + b > c and a + c > b and c + b > a:
        return True
    return False


def area(a, b, c):
    """
    Принимает переменные a, b и c, стороны треугольника
    И возвращает его площадь, если треугольник существует
    -1 если нет
    Пример вызова:
    area(3, 4, 5)
    Возвращаемое значение:
    8
    """
    half_per = (a + b + c) / 2
    if existing(a, b, c):
        return (half_per * (half_per - a) * (half_per - b) * (half_per - c)) ** 0.5
    return -1


def perimeter(a, b, c):
    """
    Принимает переменные a, b и c, стороны треугольника
    И возвращает его периметр, если треугольник существует
    -1, если нет
    Пример вызова:
    perimeter(1, 1, 1)
    Возвращаемое значение:
    3
    """
    if existing(a, b, c):
        return a + b + c
    return -1


class TriangleTestCase(unittest.TestCase):

    def test_perimetr_1(self):
        res = perimeter(2, 2, 3)
        self.assertEqual(res, 2 + 2 + 3)

    def test_perimetr_2(self):
        res = area(-1, 2, -3)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(-1, 2, -3)")

    def test_perimetr_3(self):
        self.assertRaises(TypeError, perimeter, 1, 2, 3, 4,  "Fail test number 3, perimetr(1, 2, 3, 4)")

    def test_perimetr_4(self):
        self.assertRaises(TypeError, perimeter, 1, 2, "a",  "Fail test number 4, perimetr(1, 2, a)")

    def test_perimetr_5(self):
        res = perimeter(1000000000000, 4, 4)
        self.assertEqual(res, -1, "Fail test number 5, perimetr(1000000000000, 4, 4)")

    def test_area_1(self):
        res = area(1, 2, 2)
        half_per = (1 + 2 + 2) / 2
        self.assertEqual(res, (half_per * (half_per - 1) * (half_per - 2) * (half_per - 2)) ** 0.5,
                         "Fail test number 1, area(1, 2, 2)")

    def test_area_2(self):
        res = area(2, 4, -1)
        self.assertEqual(res, "Фигура не существует", "Fail test number 2, area(2, 4, -1)")

    def test_area_3(self):
        self.assertRaises(TypeError, perimeter, 1, 2, 3, 4,  "Fail test number 3, area(1, 2, 3, 4)")

    def test_area_4(self):
        self.assertRaises(TypeError, perimeter, 1, 2, "a",  "Fail test number 4, area(1, 2, a)")

    def test_area_5(self):
        res = area(1000000000000, 4, 4)
        self.assertEqual(res, -1, "Fail test number 5, area(1000000000000, 4, 4)")