'''Считает параметры круга, принимая на вход его радиус'''
import math
import unittest


def area(r):
    '''
    Принимает радиус, возвращает площадь
        Пример вывода:
            10
            314.1592653589793
    '''
    
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус, возвращает периметр
        Пример вывода:
            10
            62.83185307179586
    '''

    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_area_positive(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_area_negative(self):
        res = area(-10)
        self.assertEqual(res, 314.1592653589793)
    
    def test_area_fractional(self):
        res = area(0.5)
        self.assertEqual(res, 0.7853981633974483)
    
    def test_area_string(self):
        with self.assertRaises(TypeError):
            area('abc')

    
    
    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
       
    def test_perimeter_one(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_perimeter_positive(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_negative(self):
        res = perimeter(-10)
        self.assertEqual(res, -62.83185307179586)
    
    def test_perimeter_fractional(self):
        res = perimeter(0.5)
        self.assertEqual(res, 3.141592653589793)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            perimeter('abc')