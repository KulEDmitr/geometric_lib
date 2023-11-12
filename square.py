import unittest
def area(a):
    '''
    Функция принимает на вход десятичное натуральное число и возвращает десятичное натуральное число равное площади квадрата, сторона которого равна данному числу.
    Пример: area(10) = 100
    '''
    return a * a


def perimeter(a):
    '''
    
    Функция принимает на вход десятичное натуральное число и возвращает десятичное натуральное число равное периметру квадрата, сторона которого равна данному числу.
    Пример:perimeter(10) = 40
    
    '''
    return 4 * a

class ScuareTestCase(unittest.TestCase):
    def test_zero_arg(self):
        with self.assertRaises(ValueError):
            area(0)
            perimeter(0)
    def test_random(self):
        self.assertEqual(area(64), 4096)
        self.assertEqual(perimeter(298), 1192)
    def test_float(self):
        self.assertEqual(area(0.3), 0.3*0.3)
        self.assertEqual(perimeter(0.3), 4*0.3)
    def test_wrong_value(self):
        with self.assertRaises(TypeError):
            area('dkkd')
        with self.assertRaises(TypeError):
            perimeter('dkkd')
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            area(-20)
        with self.assertRaises(ValueError):
            perimeter(-400)