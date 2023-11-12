import unittest

def area(a, b): 
    '''
    
    Функция принимает на вход два десятичных натуральных числа a,b и возвращает десятичное натуральное число, площадь прямоугольника, длина сторон которого соответственно равна данным числам
    Пример:area(10, 20) = 200
    
    '''
    return a * b 

def perimeter(a, b):
    '''
    
    Функция принимает на вход два десятичных натуральных числа a,b и возвращает десятичное натуральное число, периметр прямоугольника, длина сторон которого соответственно равна данным числам
    Пример: perimeter(10, 20) = 60
    
    '''
    return 2*a + 2*b


class RectangleTestCase(unittest.TestCase):
    def test_zero_arg(self):
        with self.assertRaises(ValueError):
            area(0, 0)
            perimeter(0, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        self.assertEqual(perimeter(10, 10), 40)

    def test_equals(self):
        res = area(10, 6)
        res2 = area(6, 10)
        self.assertEqual(res, res2)
        self.assertEqual(perimeter(10, 6), perimeter(6, 10))

    def test_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 10)
        with self.assertRaises(ValueError):
            perimeter(-10, 10)

    def test_negative2(self):
        with self.assertRaises(ValueError):
            area(10, -10)
        with self.assertRaises(ValueError):
            perimeter(10, -10)

    def test_incorrect_value(self):
        with self.assertRaises(ValueError):
            area('djka', 10)
        with self.assertRaises(ValueError):
            perimeter('djka', 10)
        
        

        
