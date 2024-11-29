import unittest
from square import area, perimeter

class TestSquareFunctions(unittest.TestCase):

    # Тестируем корректность вычисления площади квадрата
    def test_area_valid(self):
        # Проверяем стандартные значения
        self.assertEqual(area(10), 100)  # Площадь квадрата со стороной 10
        self.assertEqual(area(7.5), 56.25)  # Площадь квадрата со стороной 7.5
        self.assertEqual(area(1), 1)  # Площадь квадрата со стороной 1

    # Тестируем некорректные входные значения для площади
    def test_area_invalid(self):
        # Тестируем, когда передается строка
        with self.assertRaises(ValueError):
            area("10")  # Передаем строку вместо числа

        # Тестируем, когда передается список
        with self.assertRaises(ValueError):
            area([10])  # Передаем список вместо числа

        # Тестируем, когда передается None
        with self.assertRaises(ValueError):
            area(None)  # Передаем None вместо числа

        # Тестируем, когда передается отрицательное значение
        with self.assertRaises(ValueError):
            area(-10)  # Длина стороны не может быть отрицательной

        # Тестируем, когда передается нулевая длина стороны
        with self.assertRaises(ValueError):
            area(0)  # Длина стороны не может быть равна нулю

    # Тестируем корректность вычисления периметра квадрата
    def test_perimeter_valid(self):
        # Проверяем стандартные значения
        self.assertEqual(perimeter(10), 40)  # Периметр квадрата со стороной 10
        self.assertEqual(perimeter(7.5), 30)  # Периметр квадрата со стороной 7.5
        self.assertEqual(perimeter(1), 4)  # Периметр квадрата со стороной 1

    # Тестируем некорректные входные значения для периметра
    def test_perimeter_invalid(self):
        # Тестируем, когда передается строка
        with self.assertRaises(ValueError):
            perimeter("10")  # Передаем строку вместо числа

        # Тестируем, когда передается список
        with self.assertRaises(ValueError):
            perimeter([10])  # Передаем список вместо числа

        # Тестируем, когда передается None
        with self.assertRaises(ValueError):
            perimeter(None)  # Передаем None вместо числа

        # Тестируем, когда передается отрицательное значение
        with self.assertRaises(ValueError):
            perimeter(-10)  # Длина стороны не может быть отрицательной

        # Тестируем, когда передается нулевая длина стороны
        with self.assertRaises(ValueError):
            perimeter(0)  # Длина стороны не может быть равна нулю

if __name__ == '__main__':
    unittest.main()