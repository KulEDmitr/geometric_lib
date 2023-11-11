import random
import unittest

def area(a:int):
    '''
    Возвращает площадь квадрата в десятичном формате

        Параметры:
        а (int) - сторона квадрата в десятичном формате

        Возвращаемое значение:
        area (int) - Площадь квадрата в десятичном формате

        Примеры вызова:
        print(area(2))   \\ 4
        print(area(4))   \\ 16
        print(area(5))   \\ 25  
    '''
    if a < 0:
        raise ValueError("Side cannot be negative")
    return a * a


def perimeter(a:int):
    '''
    Возвращает периметр квадрата в десятичном формате

        Параметры:
        а (int) - сторона квадрата в десятичном формате

        Возвращаемое значение:
        perimeter (int) - периметр квадрата в десятичном формате

        Примеры вызова:
        print(perimeter(2))   \\ 8
        print(perimeter(4))   \\ 16
        print(perimeter(5))   \\ 20
    '''
    if a < 0:
        raise ValueError("Side cannot be negative")
    return 4 * a

class SquareTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def test_area_zero_side(self):
       '''
       Тестируем площадь при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(area(0), 0)
       
    def test_area_one_side(self):
        '''
       Тестируем площадь при стороне равной 1. Ожидаемый результат 1
       '''
        self.assertEqual(area(1), 1)

    def test_area_ten_side(self):
       '''
       Тестируем площадь при стороне равной 10. Ожидаемый результат 100
       '''
       self.assertEqual(area(10), 100)

    def test_area_negative_side(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_incorrect_side(self):
        '''
       Тестируем площадь при стороне равной 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            area('a')

    def test_perimeter_zero_side(self):
       '''
       Тестируем периметер при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(perimeter(0), 0)
       
    def test_perimeter_one_side(self):
        '''
       Тестируем периметер при стороне равной 1. Ожидаемый результат 4
       '''
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_ten_side(self):
       '''
       Тестируем периметер при стороне равной 10. Ожидаемый результат 40
       '''
       self.assertEqual(perimeter(10), 40)

    def test_perimeter_negative_side(self):
        '''
       Тестируем периметер при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_incorrect_side(self):
        '''
       Тестируем периметер при стороне равной 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            perimeter('a')

    def test_area_random_side(self):
        '''
        Тестируем площадь при случайных значениях радиуса. Ожидаемый результат a * a.
        '''
        for i in range(100):
            random.seed(i)
            a = random.uniform(0, 1000000)
            self.assertEqual(area(a), a * a)
    
    def test_perimeter_random_side(self):
        '''
        Тестируем периметер при случайных значениях радиуса. Ожидаемый результат 4 * a.
        '''
        for i in range(100):
            random.seed(i)
            a = random.uniform(0, 1000000)
            self.assertEqual(perimeter(a), 4 * a)