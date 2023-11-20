import unittest

class SquareTestCase(unittest.TestCase):
    def test_area_0(self):
        result = area(0)
        self.assertEqual(result, 0)
    def test_area_1(self):
        result = area(10)
        self.assertEqual(result, 100)
    def test_area_2(self):
        result = area(12356)
        self.assertEqual(result, 152670736)
    def test_area_3(self):
        result = area(-19)
        self.assertEqual(result, "face can't be less than 0!")
    def test_area_4(self):
        result = area(2147483647)
        self.assertEqual(result, 4611686014132420609)

    def test_perimeter_0(self):
        result = perimeter(0)
        self.assertEqual(result, 0)
    def test_perimeter_1(self):
        result = perimeter(10)
        self.assertEqual(result, 40)
    def test_perimeter_2(self):
        result = perimeter(12356)
        self.assertEqual(result, 49424)
    def test_perimeter_3(self):
        result = perimeter(-19)
        self.assertEqual(result, "face can't be less than 0!")
    def test_perimeter_4(self):
        result = perimeter(2147483647)
        self.assertEqual(result, 8589934588)

def area(a):
    '''
    Возвращает площадь квадрата.

        Параметры:
            a (int): длина стороны квадрата

        Возвращаемое значение:
            area (int): площадь квадрата

        Пример вызова:
            area(3) = 9
    '''
    if a < 0:
        return "face can't be less than 0!"
    else:
        return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата.

        Параметры:
            a (int): длина стороны квадрата

        Возвращаемое значение:
            perimeter (int): периметр квадрата

        Пример вызова:
            perimeter(3) = 12
    '''
    if a < 0:
        return "face can't be less than 0!"
    else:
        return 4 * a
