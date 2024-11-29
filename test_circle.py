import unittest
import math
from circle import area, perimeter

class TestCircleFunctions(unittest.TestCase):

    # Тест для функции area
    def test_area_valid(self):
        # Проверим правильность вычислений для площади круга
        self.assertAlmostEqual(area(10), math.pi * 10 * 10)  # Площадь круга с радиусом 10
        self.assertAlmostEqual(area(7.5), math.pi * 7.5 * 7.5)  # Площадь круга с радиусом 7.5

    def test_area_invalid(self):
        # Тестируем случай, когда радиус не является числом
        with self.assertRaises(ValueError):
            area("10")  # Передаем строку вместо числа
        with self.assertRaises(ValueError):
            area([10])  # Передаем список вместо числа
        with self.assertRaises(ValueError):
            area(None)  # Передаем None вместо числа
        # Тестируем случай с отрицательным значением радиуса
        with self.assertRaises(ValueError):
            area(-10)  # Передаем отрицательное значение

    # Тест для функции perimeter
    def test_perimeter_valid(self):
        # Проверим правильность вычислений для периметра круга
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10)  # Периметр круга с радиусом 10
        self.assertAlmostEqual(perimeter(7.5), 2 * math.pi * 7.5)  # Периметр круга с радиусом 7.5

    def test_perimeter_invalid(self):
        # Тестируем случай, когда радиус не является числом
        with self.assertRaises(ValueError):
            perimeter("10")  # Передаем строку вместо числа
        with self.assertRaises(ValueError):
            perimeter([10])  # Передаем список вместо числа
        with self.assertRaises(ValueError):
            perimeter(None)  # Передаем None вместо числа
        # Тестируем случай с отрицательным значением радиуса
        with self.assertRaises(ValueError):
            perimeter(-10)  # Передаем отрицательное значение

if __name__ == '__main__':
    unittest.main()