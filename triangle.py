import unittest
import random

def area(a:int, h:int):
    '''
    Возвращает площадь треугольника в десятичном формате

        Параметры:
        а (int) - основание треугольника в десятичном формате
        h (int) - высота треугольника в десятичном формате

        Возвращаемое значение:
        area (int) - Площадь треугольника в десятичном формате

        Примеры вызова:
        print(area(2, 1))    \\ 1
        print(area(4, 3))    \\ 6
        print(area(5, 10))   \\ 25
    '''
    if a < 0 or h < 0:
        raise ValueError("Sides cannot be less than zero")
    return a * h / 2

def perimeter(a:int, b:int, c:int):
    '''
    Возвращает периметр треугольника в десятичном формате

        Параметры:
        а (int) - 1 сторона треугольника в десятичном формате
        b (int) - 2 сторона треугольника в десятичном формате
        c (int) - 3 сторона треугольника в десятичном формате

        Возвращаемое значение:
        perimeter (int) - периметр треугольника в десятичном формате

        Примеры вызова:
        print(perimeter(2, 5, 4))   \\ 11
        print(perimeter(4, 4, 1))   \\ 9
        print(perimeter(5, 5, 3))   \\ 13
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Sides cannot be less than zero")
    if a == 0 or b == 0 or c == 0:
        return 0
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def test_area_zero_height(self):
        '''
        Тестируем площадь при высоте равной 0. Ожидаемый результат 0
        '''
        self.assertEqual(area(20, 0), 0)
    
    def test_area_zero_base(self):
        '''
        Тестируем площадь при основании равном 0. Ожидаемый результат 0
        '''
        self.assertEqual(area(0, 20), 0)

    def test_area_one_height(self):
        '''
        Тестируем площадь при высоте равной 1. Ожидаемый результат 10.
        '''
        self.assertEqual(area(20, 1), 10)
    
    def test_area_one_base(self):
        '''
        Тестируем площадь при основании равном 1. Ожидаемый резьтат 10.
        '''
        self.assertEqual(area(1, 20), 10)
    
    def test_area_negative_height(self):
        '''
        Тестируем площадь при отрицательной высоте. Ожидаемый результат ошибка
        '''
        with self.assertRaises(ValueError):
            area(10, -1)

    def test_area_negative_base(self):
        '''
        Тестируем площадь при отрицательном основании. Ожидаемый результат ошибка
        '''
        with self.assertRaises(ValueError):
            area(-1, 10)

    def test_area_incorrect_height(self):
        '''
        Тестируем площадь при неправильной высоте. Ожидаемый результат ошибка
        '''
        with self.assertRaises(TypeError):
            area(10, 'a')

    def test_area_incorrect_base(self):
        '''
        Тестируем площадь при неправильном основании. Ожидаемый результат ошибка
        '''
        with self.assertRaises(TypeError):
            area('a', 10)
    
    def test_perimeter_zero_side1(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(perimeter(0, 1, 1), 0)

    def test_perimeter_zero_side2(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(perimeter(1, 0, 1), 0)

    def test_perimeter_zero_side3(self):
        '''
        Тестируем периметр при одной из сторон равной 0
        '''
        self.assertEqual(perimeter(1, 1, 0), 0)

    def test_perimeter_random_sides(self):
        '''
        Тестируем периметр при рандомных сторонах
        '''
        a = random.uniform(0, 1000000)
        b = random.uniform(0, 1000000)
        c = random.uniform(0, 1000000)
        self.assertEqual(perimeter(a, b, c), a + b + c)

    def test_perimeter_negative_side1(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            perimeter(-1, 0, 0)

    def test_perimeter_negative_side2(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            perimeter(0, -1, 0)

    def test_perimeter_negative_side3(self):
        '''
        Тестируем периметр при одной из сторон равной -1
        '''
        with self.assertRaises(ValueError):
            perimeter(0, 0, -1)

    def test_perimeter_incorrect_side1(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            perimeter('a', 0, 0)

    def test_perimeter_incorrect_side2(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            perimeter(0, 'a', 0)

    def test_perimeter_incorrect_side3(self):
        '''
        Тестируем периметр при одной из сторон равной 'a'
        '''
        with self.assertRaises(TypeError):
            perimeter(0, 0, 'a')