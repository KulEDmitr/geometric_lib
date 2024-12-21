import unittest
from rectangle import area, perimeter  # Импортируем функции area и perimeter

class TriangleTestCase(unittest.TestCase):
    #тестируем корректные значения
    def test_area(self):
        self.assertEqual(area(5, 4), 20)  # Проверяем, area =  20
        self.assertEqual(area(0, 10), 0)  # Проверяем, area =  0
        self.assertEqual(area(10, 0), 0)  # Проверяем, area =  0
        self.assertEqual(area(3, 6), 18)    # Проверяем, area =  18

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)  # Проверяем, perimeter =  9
        self.assertEqual(perimeter(1, 0), 2)  # Проверяем, perimeter =  0
        self.assertEqual(perimeter(0, 0), 0)   # Проверяем, perimeter =  0

    # Тестируем некорректные входные данные 
    def test_invalid_area(self):
        with self.assertRaises(TypeError):
            area("5", 4)  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(TypeError):
            area(5, "4")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            area(-5, 4)   # Проверяем, что отрицательное основание вызывает ошибку
        with self.assertRaises(ValueError):
            area(5, -4)   # Проверяем, что отрицательная высота вызывает ошибку
        with self.assertRaises(ValueError):
            area(1e308, 1e308)  # Проверяем, что слишком большие числа вызывают ошибку

    def test_invalid_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("2", 3)  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(TypeError):
            perimeter(2, "3")  # Проверяем, что строка вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(-2, 3)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(2, -3)   # Проверяем, что отрицательная сторона вызывает ошибку
        with self.assertRaises(ValueError):
            perimeter(1e308, 1e308)  # Проверяем, что слишком большие числа вызывают ошибку

if __name__ == '__main__':
    unittest.main()
