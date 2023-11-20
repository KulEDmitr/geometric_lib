import unittest

class RectangleTestCase(unittest.TestCase):
    def test_area_0(self):
        result = area(0, 0)
        self.assertEqual(result, 0)
    def test_area_1(self):
        result = area(0, 10)
        self.assertEqual(result, 0)
    def test_area_2(self):
        result = area(12, 356)
        self.assertEqual(result, 4272)
    def test_area_3(self):
        result = area(-19, 33)
        self.assertEqual(result, "face can't be less than 0!")
    def test_area_4(self):
        result = area(2147483647, 2147483647)
        self.assertEqual(result, 4611686014132420609)

    def test_perimeter_0(self):
        result = perimeter(0, 0)
        self.assertEqual(result, 0)
    def test_perimeter_1(self):
        result = perimeter(0, 10)
        self.assertEqual(result, 0)
    def test_perimeter_2(self):
        result = perimeter(12, 356)
        self.assertEqual(result, 736)
    def test_perimeter_3(self):
        result = perimeter(-19, 33)
        self.assertEqual(result, "face can't be less than 0!")
    def test_perimeter_4(self):
        result = perimeter(2147483647, 2147483647)
        self.assertEqual(result, 8589934588)

def area(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a (int): длина одной стороны прямоугольника
            b (int): длина другой стороны прямоугольника

        Возвращаемое значение:
            area (int): площадь прямоугольика

        Пример вызова:
            area(2, 5) = 10
    '''
    if a < 0 or b < 0:
        return "face can't be less than 0!"
    else:
        return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

        Параметры:
            a (int): длина одной стороны прямоугольника
            b (int): длина другой стороны прямоугольника

        Возвращаемое значение:
            perimeter (int): периметр прямоугольика

        Пример вызова:
            perimeter(2, 5) = 14
    '''
    if a < 0 or b < 0:
        return "face can't be less than 0!"
    else:
        return 2 * (a + b)