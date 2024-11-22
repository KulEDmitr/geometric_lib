'''Возвращает параметры квадрата, принимая на вход одну его сторону'''
import unittest



def area(a):
    '''
    Принимает сторону квадрата,
    возвращает его площадь
        Пример вывода:
            10
            100
    '''

    return a * a


def perimeter(a):
    '''
    Принимает сторону квадрата,
    возвращает его периметр
        Пример вывода:
            10
            40
    '''
    
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_positive(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, 100)
    
    def test_area_fractional(self):
        res = area(0.5)
        self.assertEqual(res, 0.25)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area('abc')
        
    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
       
    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertEqual(res, -40)
    
    def test_perimeter_fractional(self):
        res = perimeter(0.5)
        self.assertEqual(res, 2)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            perimeter('abc')