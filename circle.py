import math
import unittest

def area(r):
    '''
    
    Функция получает на вход значение радиуса круга(десятичное натуральное число) и возвращает десятичное число, значение площади круга с данным радиусом
    Пример: area(10)=314
    
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    
    Функция получает на вход значение радиуса окружности(десятичное натуральное число) и возвращает десятичное число, значение длины окружности с данным радиусом
    Пример: perimeter(10) = 62,8
    
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_arg(self):
        with self.assertRaises(ValueError):
            area(0)
            perimeter(0)
    def test_random(self):
        self.assertEqual(area(650), math.pi*650*650)
        self.assertEqual(perimeter(650), 2*math.pi*650)
    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            area('dkkd')
        with self.assertRaises(ValueError):
            perimeter('dkkd')
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            area(-100)
        with self.assertRaises(ValueError):
            perimeter(-100)


