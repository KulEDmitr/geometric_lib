import unittest

from triangle import area, perimeter

class TestTriangleFunctions(unittest.TestCase):

    # Тестируем корректность вычисления площади треугольника
    def test_area_valid(self):
        # Проверяем стандартные значения
        self.assertEqual(area(10, 5), 25.0)  # Площадь треугольника с основанием 10 и высотой 5
        self.assertEqual(area(7.5, 4), 15.0)  # Площадь треугольника с основанием 7.5 и высотой 4

    # Тестируем некорректные входные значения для площади
    def test_area_invalid(self):
        # Тестируем, когда передается строка вместо числа
        with self.assertRaises(ValueError):
            area("10", 5)  # Передаем строку вместо числа

        with self.assertRaises(ValueError):
            area(10, "5")  # Передаем строку вместо числа

        with self.assertRaises(ValueError):
            area("10", "5")  # Передаем строку вместо числа

        # Тестируем, когда передается отрицательное значение
        with self.assertRaises(ValueError):
            area(10, -5)  # Основание и высота должны быть положительными числами

        # Тестируем, когда передается нулевая высота
        with self.assertRaises(ValueError):
            area(10, 0)  # Основание и высота не могут быть равны нулю

    # Тестируем корректность вычисления периметра треугольника
    def test_perimeter_valid(self):
        # Проверяем стандартные значения
        self.assertEqual(perimeter(3, 4, 5), 12)  # Периметр прямоугольного треугольника
        self.assertEqual(perimeter(10, 5, 7), 22)  # Периметр треугольника с такими сторонами

    # Тестируем некорректные входные значения для периметра
    def test_perimeter_invalid(self):
        # Тестируем, когда передается строка вместо числа
        with self.assertRaises(ValueError):
            perimeter(3, 4, "5")  # Передаем строку вместо числа

        # Тестируем, когда одна из сторон отрицательная
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)  # Стороны должны быть положительными числами

        # Тестируем, когда стороны не могут составить треугольник
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)  # Стороны не могут составлять треугольник

if __name__ == '__main__':
    unittest.main()

