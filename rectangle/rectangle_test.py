import random
import unittest
from rectangle import rectangle

class RectangleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def setUp(self):
        '''
        Функция позволяет использовать класc rectangle внутри тестов
        '''
        self.rectangle = rectangle

    def test_area_zero_sides(self):
       '''
       Тестируем площадь при сторонах равных 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.area(0, 0), 0)
       
    def test_area_zero_left_side(self):
       '''
       Тестируем площадь при сторонe равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.area(10, 0), 0)

    def test_area_zero_right_side(self):
       '''
       Тестируем площадь при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.area(0, 10), 0)

    def test_area_five_sides(self):
       '''
       Тестируем площадь при сторонах равных 5. Ожидаемый результат 25. 
       '''
       self.assertEqual(self.rectangle.area(5, 5), 25)

    def test_area_ten_sides(self):
       '''
       Тестируем площадь при сторонах равных 10. Ожидаемый результат 100. 
       '''
       self.assertEqual(self.rectangle.area(10, 10), 100)

    def test_area_negative_sides(self):
        '''
       Тестируем площадь при сторонах равных -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.area(-1, -1)

    def test_area_negative_right_side(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.area(-1, 0)

    def test_area_negative_left_sides(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.area(0, -1)

    def test_area_incorrect_sides(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.area('a', 'a')

    def test_area_incorrect_left_side(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.area(0, 'a')

    def test_area_incorrect_right_side(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.area('a', 0)

    def test_perimeter_zero_sides(self):
       '''
       Тестируем периметр при сторонах равных 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.perimeter(0, 0), 0)
       
    def test_perimeter_zero_left_side(self):
       '''
       Тестируем периметр при сторонe равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.perimeter(10, 0), 0)

    def test_perimeter_zero_right_side(self):
       '''
       Тестируем периметр при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(self.rectangle.perimeter(0, 10), 0)

    def test_perimeter_five_sides(self):
       '''
       Тестируем периметр при сторонах равных 5. Ожидаемый результат 20. 
       '''
       self.assertEqual(self.rectangle.perimeter(5, 5), 20)

    def test_perimeter_ten_sides(self):
       '''
       Тестируем периметр при сторонах равных 10. Ожидаемый результат 40. 
       '''
       self.assertEqual(self.rectangle.perimeter(10, 10), 40)

    def test_perimeter_negative_sides(self):
        '''
       Тестируем периметр при сторонах равных -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.perimeter(-1, -1)

    def test_perimeter_negative_right_side(self):
        '''
       Тестируем периметр при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.perimeter(-1, 0)

    def test_perimeter_negative_left_sides(self):
        '''
       Тестируем периметр при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            self.rectangle.perimeter(0, -1)

    def test_perimeter_incorrect_sides(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.perimeter('a', 'a')

    def test_perimeter_incorrect_left_side(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.perimeter(0, 'a')

    def test_perimeter_incorrect_right_side(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            self.rectangle.perimeter('a', 0)

    