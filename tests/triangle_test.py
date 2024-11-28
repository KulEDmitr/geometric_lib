import unittest  # Импортирование модуля для юнит-тестирования
import triangle  # Импортирование модуля с функциями для вычисления площади и периметра треугольника

class TriangleTestCase(unittest.TestCase):  # Определение класса для тестирования треугольника

    def test_triangle_area_yes(self):  # Тестирование корректного расчета площади треугольника
        res = triangle.area(2, 8)  # Вычисление площади с основаниями 2 и высотой 8
        self.assertEqual(res, 8)  # Проверка, что результат равен 8

    def test_triangle_area_no(self):  # Тестирование поведения при отрицательной высоте
        res = triangle.area(2, -8)  # Вычисление площади с основаниями 2 и высотой -8
        self.assertEqual(res, -8.0)  # Проверка, что результат равен -8.0

    def test_triangle_area_real_numbers(self):  # Тестирование площади с вещественными числами
        res = triangle.area(2.75, 8.6)  # Вычисление площади с основаниями 2.75 и высотой 8.6
        self.assertEqual(res, 11.825)  # Проверка на соответствие результату 

    def test_triangle_area_zero(self):  # Тестирование площади с нулевой высотой
        res = triangle.area(2, 0)  # Вычисление площади с основаниями 2 и высотой 0
        self.assertEqual(res, 0)  # Проверка, что площадь равна 0

    def test_triangle_perimeter_yes(self):  # Тестирование корректного расчета периметра треугольника
        res = triangle.perimeter(2, 8, 11)  # Вычисление периметра с длинами сторон 2, 8, 11
        self.assertEqual(res, 21)  # Проверка, что результат равен 21

    def test_triangle_perimeter_no(self):  # Тестирование поведения при отрицательной стороне
        res = triangle.perimeter(2, -8, 11)  # Вычисление периметра с одной отрицательной стороной
        self.assertEqual(res, 5)  # Проверка, что периметр равен 5

    def test_triangle_perimeter_real_numbers(self):  # Тестирование периметра с вещественными числами
        res = triangle.perimeter(2.75, 8.6, 11)  # Вычисление периметра с длинами 2.75, 8.6, 11
        self.assertEqual(res, 22.35)  # Проверка на соответствие результату 

    def test_triangle_perimeter_zero(self):  # Тестирование периметра с нулевой стороной
        res = triangle.perimeter(2, 0, 8.59)  # Вычисление периметра с одной стороной 0
        self.assertEqual(res, 10.59)  # Проверка, что периметр равен 10.59

if __name__ == '__main__':  # Проверка, что скрипт запущен напрямую
    unittest.main()  # Запуск всех тестов
triang_test = TriangleTestCase  # Создание экземпляра тестов (необязательно)