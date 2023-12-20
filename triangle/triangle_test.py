import unittest
import random
from triangle import triangle

class TriangleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def setUp(self):
        '''
        Функция позволяет использовать класс triangle внутри тестов
        '''
        self.triangle = triangle

    def test_area_zero_height(self):
        '''
        Тестируем площадь при высоте равной 0. Ожидаемый результат 0
        '''
        self.assertEqual(self.triangle.area(20, 0), 0)
    
    def test_area_zero_base(self):
        '''
        Тестируем площадь при основании равном 0. Ожидаемый результат 0
        '''
        self.assertEqual(self.triangle.area(0, 20), 0)

    def test_area_one_height(self):
        '''
        Тестируем площадь при высоте равной 1. Ожидаемый результат 10.
        '''
        self.assertEqual(self.triangle.area(20, 1), 10)
    
    def test_area_one_base(self):
        '''
        Тестируем площадь при основании равном 1. Ожидаемый резьтат 10.
        '''
        self.assertEqual(self.triangle.area(1, 20), 10)
    
    def test_area_negative_height(self):
        '''
        Тестируем площадь при отрицательной высоте. Ожидаемый результат ошибка
        '''
        with self.assertRaises(ValueError):
            self.triangle.area(10, -1)

    def test_area_negative_base(self):
        '''
        Тестируем площадь при отрицательном основании. Ожидаемый результат ошибка
        '''
        with self.assertRaises(ValueError):
            self.triangle.area(-1, 10)

    def test_area_incorrect_height(self):
        '''
        Тестируем площадь при неправильной высоте. Ожидаемый результат ошибка
        '''
        with self.assertRaises(TypeError):
            self.triangle.area(10, 'a')

    def test_area_incorrect_base(self):
        '''
        Тестируем площадь при неправильном основании. Ожидаемый результат ошибка
        '''
        with self.assertRaises(TypeError):
            self.triangle.area('a', 10)
    
    def test_perimeter_zero_side1(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(self.triangle.perimeter(0, 1, 1), 0)

    def test_perimeter_zero_side2(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(self.triangle.perimeter(1, 0, 1), 0)

    def test_perimeter_zero_side3(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(self.triangle.perimeter(1, 1, 0), 0)

    def test_perimeter_random_sides(self):
        '''
        Тестируем периметр при рандомных сторонах
        '''
        a = random.uniform(0, 1000000)
        b = random.uniform(0, 1000000)
        c = random.uniform(0, 1000000)
        self.assertEqual(self.triangle.perimeter(a, b, c), a + b + c)

    def test_perimeter_negative_side1(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            self.triangle.perimeter(-1, 0, 0)

    def test_perimeter_negative_side2(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            self.triangle.perimeter(0, -1, 0)

    def test_perimeter_negative_side3(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            self.triangle.perimeter(0, 0, -1)

    def test_perimeter_incorrect_side1(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            self.triangle.perimeter('a', 0, 0)

    def test_perimeter_incorrect_side2(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            self.triangle.perimeter(0, 'a', 0)

    def test_perimeter_incorrect_side3(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            self.triangle.perimeter(0, 0, 'a')