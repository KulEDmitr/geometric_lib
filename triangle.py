import unittest

class TriangleTestCase(unittest.TestCase):
    def test_area_0(self):
        result = area(0, 0)
        self.assertEqual(result, 0)
    def test_area_1(self):
        result = area(0, 10)
        self.assertEqual(result, 0)
    def test_area_2(self):
        result = area(12, 356)
        self.assertEqual(result, 2136)
    def test_area_3(self):
        result = area(-19, 33)
        self.assertEqual(result, "face can't be less than 0!")
    def test_area_4(self):
        result = area(2147483647, 2147483647)
        self.assertEqual(result, 2.3058430070662103e+18)

    def test_perimeter_0(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0)
    def test_perimeter_1(self):
        result = perimeter(0, 10, 20)
        self.assertEqual(result, 0)
    def test_perimeter_2(self):
        result = perimeter(12, 356, 78)
        self.assertEqual(result, 446)
    def test_perimeter_3(self):
        result = perimeter(-19, 33, -100)
        self.assertEqual(result, "face can't be less than 0!")
    def test_perimeter_4(self):
        result = perimeter(2147483647, 2147483647, 2147483647)
        self.assertEqual(result, 6442450941)

def area(a, h):
    '''
    Возвращает площадь треугольника.

        Параметры:
            a (int): длина стороны треугольника
            b (int): высота треугольника к стороне a

        Возвращаемое значение:
            area (int): площадь треугольника

        Пример вызова:
            area(5, 4) = 10
    '''
    if a < 0 or h < 0:
        return "face can't be less than 0!"
    else:
        return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.

        Параметры:
            a (int): длина первой стороны треугольника
            b (int): длина второй стороны треугольника
            c (int): длина третьей стороны треугольника

        Возвращаемое значение:
            perimeter (int): периметр треугольника

        Пример вызова:
            perimeter(2, 2, 3) = 7
    '''
    if a < 0 or b < 0 or c < 0:
        return "face can't be less than 0!"
    else:
        return a + b + c