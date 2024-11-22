'''Возвращает параметры треугольника, принимая на вход его стороны и высоту'''
import unittest


def area(a, h):
    '''
    Принимает сторону и высоту треугольника,
    возвращает его площадь
        Пример вывода:
            10 5
            25
    '''
    
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Принимает 3 стороны треугольника,
    возвращает его периметр
        Пример вывода:
            10 10 15
            35
    '''
    
    return a + b + c


class SquareTestCase(unittest.TestCase):
    def test_area_side_zero(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_height_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_side_one(self):
        res = area(1, 10)
        self.assertEqual(res, 5)

    def test_area_height_one(self):
        res = area(10, 1)
        self.assertEqual(res, 5)

    def test_area_positive(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_area_negative(self):
        res = area(-10, 10)
        self.assertEqual(res, -50)
    
    def test_area_fractional(self):
        res = area(10, 0.5)
        self.assertEqual(res, 2.5)

    def test_area_side_string(self):
        with self.assertRaises(TypeError):
            area('abc', 10)

    def test_area_height_string(self):
        with self.assertRaises(TypeError):
            area(10, 'abc')
        
    
    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
       
    def test_perimeter_one(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_positive(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_negative(self):
        res = perimeter(-10, -10, -10)
        self.assertEqual(res, -30)
    
    def test_perimeter_fractional(self):
        res = perimeter(0.5, 0.5, 0.5)
        self.assertEqual(res, 1.5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            perimeter('abc', 'abc', 'abc')