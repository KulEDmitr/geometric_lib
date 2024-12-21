import unittest
from square import area, perimeter  # Импортируем функции area и perimeter

class TriangleTestCase(unittest.TestCase):
    #тестируем корректные значения
    def test_area(self):
        self.assertEqual(area(5), 25)  # Проверяем, area =  25
        self.assertEqual(area(0), 0)  # Проверяем, area =  0

    def test_perimeter(self):
        self.assertEqual(perimeter(2), 8)  # Проверяем, perimeter =  8
        self.assertEqual(perimeter(1), 4)  # Проверяем, perimeter =  4
        self.assertEqual(perimeter(0), 0)   # Проверяем, perimeter =  0

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
