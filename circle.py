import math
import unittest
import random

def area(r):
    '''
    Возвращает площадь круга в десятичном формате

        Параметры:
        r (int) - радиус круга в десятичном формате

        Возвращаемое значение:
        area (int) - площадь круга в десятичном формате

        Примеры вызова:
        print(area(2))  \\ 12,566370614359173
        print(area(4))  \\ 50,265482457436692
        print(area(5))  \\ 78,539816339744831
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга в десятичном формате

        Параметры:
        r (int) - радиус круга в десятичном формате

        Возвращаемое значение:
        perimetr (int) - периметр круга в десятичном формате

        Примеры вызова:
        print(perimeter(2))  \\ 12,566370614359173
        print(perimeter(4))  \\ 25,132741228718346
        print(perimeter(5))  \\ 31,415926535897932
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def test_area_zero_radius(self):
       '''
       Тестируем площадь при радиусе равном 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(area(0), 0)
       
    def test_area_one_radius(self):
        '''
       Тестируем площадь при радиусе равном 1. Ожидаемый результат 3.141592653589793
       '''
        self.assertEqual(area(1), 3.141592653589793)

    def test_area_ten_radius(self):
       '''
       Тестируем площадь при радиусе равном 10. Ожидаемый результат 314.1592653589793
       '''
       self.assertEqual(area(10), 314.1592653589793)

    def test_area_negative_radius(self):
        '''
       Тестируем площадь при радиусе равном -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            area(-1)

    def test_area_incorrect_radius(self):
        '''
       Тестируем площадь при радиусе равном 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            area('a')

    def test_perimeter_zero_radius(self):
       '''
       Тестируем периметер при радиусе равном 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(perimeter(0), 0)
       
    def test_perimeter_one_radius(self):
        '''
       Тестируем периметер при радиусе равном 1. Ожидаемый результат 3.141592653589793
       '''
        self.assertEqual(perimeter(1), 6.283185307179586)

    def test_perimeter_ten_radius(self):
       '''
       Тестируем периметер при радиусе равном 10. Ожидаемый результат 314.1592653589793
       '''
       self.assertEqual(perimeter(10), 62.83185307179586)

    def test_perimeter_negative_radius(self):
        '''
       Тестируем периметер при радиусе равном -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_incorrect_radius(self):
        '''
       Тестируем периметер при радиусе равном 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            perimeter('a')

    def test_area_random_radius(self):
        '''
        Тестируем площадь при случайных значениях радиуса. Ожидаемый результат Pi * r * r.
        '''
        for i in range(100):
            random.seed(i)
            r = random.uniform(0, 1000000)
            self.assertEqual(area(r), math.pi * r * r)
    
    def test_perimeter_random_radius(self):
        '''
        Тестируем периметер при случайных значениях радиуса. Ожидаемый результат 2 * Рi * r.
        '''
        for i in range(100):
            random.seed(i)
            r = random.uniform(0, 1000000)
            self.assertEqual(perimeter(r), 2 * math.pi * r)

