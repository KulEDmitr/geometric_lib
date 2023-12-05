import math
import unittest
import random
from circle import circle


class CircleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def setUp(self):
        '''
        Функция позволяет использовать класс circle внутри тестов
        '''
        self.circle = circle

    def test_area_zero_radius(self):
       '''
       Тестируем площадь при радиусе равном 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.circle.area(0), 0)
       
    def test_area_one_radius(self):
        '''
       Тестируем площадь при радиусе равном 1. Ожидаемый результат 3.141592653589793
       '''
        self.assertEqual(self.circle.area(1), 3.141592653589793)

    def test_area_ten_radius(self):
       '''
       Тестируем площадь при радиусе равном 10. Ожидаемый результат 314.1592653589793
       '''
       self.assertEqual(self.circle.area(10), 314.1592653589793)

    def test_area_negative_radius(self):
        '''
       Тестируем площадь при радиусе равном -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.circle.area(-1)

    def test_area_incorrect_radius(self):
        '''
       Тестируем площадь при радиусе равном 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.circle.area('a')

    def test_perimeter_zero_radius(self):
       '''
       Тестируем периметер при радиусе равном 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.circle.perimeter(0), 0)
       
    def test_perimeter_one_radius(self):
        '''
       Тестируем периметер при радиусе равном 1. Ожидаемый результат 3.141592653589793
       '''
        self.assertEqual(self.circle.perimeter(1), 6.283185307179586)

    def test_perimeter_ten_radius(self):
       '''
       Тестируем периметер при радиусе равном 10. Ожидаемый результат 314.1592653589793
       '''
       self.assertEqual(self.circle.perimeter(10), 62.83185307179586)

    def test_perimeter_negative_radius(self):
        '''
       Тестируем периметер при радиусе равном -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.circle.perimeter(-1)

    def test_perimeter_incorrect_radius(self):
        '''
       Тестируем периметер при радиусе равном 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.circle.perimeter('a')

    def test_area_random_radius(self):
        '''
        Тестируем площадь при случайных значениях радиуса. Ожидаемый результат Pi * r * r.
        '''
        for i in range(100):
            random.seed(i)
            r = random.uniform(0, 1000000)
            self.assertEqual(self.circle.area(r), math.pi * r * r)
    
    def test_perimeter_random_radius(self):
        '''
        Тестируем периметер при случайных значениях радиуса. Ожидаемый результат 2 * Рi * r.
        '''
        for i in range(100):
            random.seed(i)
            r = random.uniform(0, 1000000)
            self.assertEqual(self.circle.perimeter(r), 2 * math.pi * r)