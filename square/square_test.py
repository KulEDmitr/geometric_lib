import random
import unittest
from square import square

class SquareTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def setUp(self):
        '''
        Функция позволяет использовать класc square внутри тестов
        '''
        self.square = square

    def test_area_zero_side(self):
       '''
       Тестируем площадь при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.square.area(0), 0)
       
    def test_area_one_side(self):
        '''
       Тестируем площадь при стороне равной 1. Ожидаемый результат 1
       '''
        self.assertEqual(self.square.area(1), 1)

    def test_area_ten_side(self):
       '''
       Тестируем площадь при стороне равной 10. Ожидаемый результат 100
       '''
       self.assertEqual(self.square.area(10), 100)

    def test_area_negative_side(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.square.area(-1)

    def test_area_incorrect_side(self):
        '''
       Тестируем площадь при стороне равной 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.square.area('a')

    def test_perimeter_zero_side(self):
       '''
       Тестируем периметер при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.square.perimeter(0), 0)
       
    def test_perimeter_one_side(self):
        '''
       Тестируем периметер при стороне равной 1. Ожидаемый результат 4
       '''
        self.assertEqual(self.square.perimeter(1), 4)

    def test_perimeter_ten_side(self):
       '''
       Тестируем периметер при стороне равной 10. Ожидаемый результат 40
       '''
       self.assertEqual(self.square.perimeter(10), 40)

    def test_perimeter_negative_side(self):
        '''
       Тестируем периметер при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.square.perimeter(-1)

    def test_perimeter_incorrect_side(self):
        '''
       Тестируем периметер при стороне равной 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.square.perimeter('a')

    def test_area_random_side(self):
        '''
        Тестируем площадь при случайных значениях радиуса. Ожидаемый результат a * a.
        '''
        for i in range(100):
            random.seed(i)
            a = random.uniform(0, 1000000)
            self.assertEqual(self.square.area(a), a * a)
    
    def test_perimeter_random_side(self):
        '''
        Тестируем периметер при случайных значениях радиуса. Ожидаемый результат 4 * a.
        '''
        for i in range(100):
            random.seed(i)
            a = random.uniform(0, 1000000)
            self.assertEqual(self.square.perimeter(a), 4 * a)