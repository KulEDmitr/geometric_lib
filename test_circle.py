import unittest
import math
from circle import area, perimeter  # Импортируем функции area и perimeter

class TriangleTestCase(unittest.TestCase):
    #тестируем корректные значения
    def test_area(self):
        self.assertEqual(area(4), 16*math.pi)  # Проверяем, area
        self.assertEqual(area(0), 0)  # Проверяем, area =  0
        self.assertEqual(area(1), math.pi)    # Проверяем, area =  pi

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 8*math.pi)  # Проверяем, perimeter
        self.assertEqual(perimeter(1), 2*math.pi)  # Проверяем, perimeter =  pi

    # Тестируем некорректные входные данные 
    def test_invalid_area(self):
        with self.assertRaises(TypeError):
            area("5")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            area(-5)   # Проверяем, что отрицательное основание вызывает ошибку
        with self.assertRaises(ValueError):
            area(1e308)  # Проверяем, что слишком большие числа вызывают ошибку

    def test_invalid_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("2")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(-2)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(1e308)  # Проверяем, что слишком большие числа вызывают ошибку

if __name__ == '__main__':
    unittest.main()