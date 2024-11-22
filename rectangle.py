'''
Возвращает параметры прямоугольника, принимая
на вход длины двух его сторон
'''
import unittest

def area(a, b):
    '''
    Принимает длины двух не противоположных сторон,
    возвращает площадь прямоугольника
        Пример вывода:
            10 15
            150
    '''
    
    return a * b 


def perimeter(a, b):
    '''
    Принимает длины двух не противоположных сторон,
    возвращает приметр прямоугольника
        Пример вывода:
            10 15
            50
    '''
    
    return 2*(a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_one(self):
        res = area(10, 1)
        self.assertEqual(res, 10)

    def test_area_positive(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_area_negative(self):
        res = area(10, -10)
        self.assertEqual(res, -100)
    
    def test_area_fractional(self):
        res = area(10, 0.5)
        self.assertEqual(res, 5)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            area(10, 'abc')

        
    
    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
       
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_one(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)

    def test_perimeter_positive(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_negative(self):
        res = perimeter(10, -10)
        self.assertEqual(res, 0)
    
    def test_perimeter_fractional(self):
        res = perimeter(10, 0.5)
        self.assertEqual(res, 21)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter(10, 'abc')