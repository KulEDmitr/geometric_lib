import random
import unittest

def area(a:int, b:int):
    '''
    Возвращает площадь прямоугольника в десятичном формате

        Параметры:
        а (int) - первая сторона прямоугольника в десятичном формате
        b (int) - вторая сторона прямоугольника в десятичном формате

        Возвращаемое значение:
        area (int) - Площадь прямоугольника в десятичном формате

        Примеры вызова:
        print(area(2, 3))   \\ 6
        print(area(4, 1.5)) \\ 6
        print(area(5, 5))   \\ 25
    '''
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")
    return a * b


def perimeter(a:int, b:int):
    '''
    Возвращает периметр прямоугольника в десятичном формате

        Параметры:
        а (int) - первая сторона прямоугольника в десятичном формате
        b (int) - вторая сторона прямоугольника в десятичном формате

        Возвращаемое значение:
        perimeter (int) - периметр прямоугольника в десятичном формате

        Пример вызова:
        print(perimeter(2, 3))   \\ 12
        print(perimeter(4, 1.5)) \\ 15
        print(perimeter(5, 5))   \\ 20
    '''
    if a < 0 or b < 0:
        raise ValueError("Sides cannot be negative")
    if a == 0 or b == 0:
        return 0
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    '''
    Класс наследник unittest для тестирования функций описанных выше в этом файле.
    '''
    def test_area_zero_sides(self):
       '''
       Тестируем площадь при сторонах равных 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(area(0, 0), 0)
       
    def test_area_zero_left_side(self):
       '''
       Тестируем площадь при сторонe равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(area(10, 0), 0)

    def test_area_zero_right_side(self):
       '''
       Тестируем площадь при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(area(0, 10), 0)

    def test_area_five_sides(self):
       '''
       Тестируем площадь при сторонах равных 5. Ожидаемый результат 25. 
       '''
       self.assertEqual(area(5, 5), 25)

    def test_area_ten_sides(self):
       '''
       Тестируем площадь при сторонах равных 10. Ожидаемый результат 100. 
       '''
       self.assertEqual(area(10, 10), 100)

    def test_area_negative_sides(self):
        '''
       Тестируем площадь при сторонах равных -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            area(-1, -1)

    def test_area_negative_right_side(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            area(-1, 0)

    def test_area_negative_left_sides(self):
        '''
       Тестируем площадь при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            area(0, -1)

    def test_area_incorrect_sides(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            area('a', 'a')

    def test_area_incorrect_left_side(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            area(0, 'a')

    def test_area_incorrect_right_side(self):
        '''
       Тестируем площадь при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            area('a', 0)

    def test_perimeter_zero_sides(self):
       '''
       Тестируем периметр при сторонах равных 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(perimeter(0, 0), 0)
       
    def test_perimeter_zero_left_side(self):
       '''
       Тестируем периметр при сторонe равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(perimeter(10, 0), 0)

    def test_perimeter_zero_right_side(self):
       '''
       Тестируем периметр при стороне равной 0. Ожидаемый результат 0. 
       '''
       self.assertEqual(perimeter(0, 10), 0)

    def test_perimeter_five_sides(self):
       '''
       Тестируем периметр при сторонах равных 5. Ожидаемый результат 20. 
       '''
       self.assertEqual(perimeter(5, 5), 20)

    def test_perimeter_ten_sides(self):
       '''
       Тестируем периметр при сторонах равных 10. Ожидаемый результат 40. 
       '''
       self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_negative_sides(self):
        '''
       Тестируем периметр при сторонах равных -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            perimeter(-1, -1)

    def test_perimeter_negative_right_side(self):
        '''
       Тестируем периметр при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            perimeter(-1, 0)

    def test_perimeter_negative_left_sides(self):
        '''
       Тестируем периметр при стороне равной -1. Ожидаемый результат ошибка
       '''
        with self.assertRaises(ValueError):
            perimeter(0, -1)

    def test_perimeter_incorrect_sides(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            perimeter('a', 'a')

    def test_perimeter_incorrect_left_side(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            perimeter(0, 'a')

    def test_perimeter_incorrect_right_side(self):
        '''
       Тестируем периметр при сторонах равных 'a'. Ожидаемый результат ошибка
       '''
        with self.assertRaises(TypeError):
            perimeter('a', 0)

    