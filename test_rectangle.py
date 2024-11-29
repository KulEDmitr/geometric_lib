import unittest
from rectangle import area, perimeter

class TestRectangleFunctions(unittest.TestCase):

    # Тестируем корректность вычисления площади прямоугольника
    def test_area_valid(self):
        self.assertEqual(area(10, 5), 50)  # Площадь прямоугольника с длиной 10 и шириной 5
        self.assertEqual(area(7.5, 3.2), 24.0)  # Площадь прямоугольника с такими размерами

    # Тестируем некорректные входные значения для площади
    def test_area_invalid(self):
        with self.assertRaises(ValueError):
            area("10", 5)  # Строка вместо числа

        with self.assertRaises(ValueError):
            area(0, 5)  # Нулевая длина

        with self.assertRaises(ValueError):
            area(-10, 5)  # Отрицательная длина

    # Тестируем корректность вычисления периметра прямоугольника
    def test_perimeter_valid(self):
        self.assertEqual(perimeter(10, 5), 30)  # Периметр прямоугольника с длиной 10 и шириной 5
        self.assertEqual(perimeter(7.5, 3.2), 21.4)  # Периметр прямоугольника с такими размерами

    # Тестируем некорректные входные значения для периметра
    def test_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter("10", 5)  # Строка вместо числа

        with self.assertRaises(ValueError):
            perimeter(0, 5)  # Нулевая длина

        with self.assertRaises(ValueError):
            perimeter(-10, 5)  # Отрицательная длина

if __name__ == '__main__':
    unittest.main()