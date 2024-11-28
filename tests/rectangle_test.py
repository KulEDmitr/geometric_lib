import unittest  # Импортирование модуля для юнит-тестирования
import rectangle  # Импортирование модуля с функциями для вычисления площади и периметра прямоугольника

class RectangleTestCase(unittest.TestCase):  # Определение класса тестирования для прямоугольников

    def test_rectangle_area_yes(self):  # Тестирование корректного расчета площади прямоугольника
        res = rectangle.area(4, 7)  # Вычисление площади с длиной 4 и шириной 7
        self.assertEqual(res, 28)  # Проверка на равенство с ожидаемым значением

    def test_rectangle_area_no(self):  # Тестирование поведения при отрицательном значении ширины
        res = rectangle.area(4, -7)  # Вычисление площади с отрицательной шириной
        self.assertEqual(res, -28)  # Проверка, что результат соответствует ожидаемому (некорректное поведение)

    def test_rectangle_area_real_numbers(self):  # Тестирование площади с вещественными числами
        res = rectangle.area(4.25, 7.36)  # Вычисление площади с длиной 4.25 и шириной 7.36
        self.assertEqual(res, 31.28)  # Проверка на соответствие результата

    def test_rectangle_area_zero(self):  # Тестирование площади с одной стороной равной нулю
        res = rectangle.area(4, 0)  # Вычисление площади при ширине 0
        self.assertEqual(res, 0)  # Проверка, что площадь равна 0

    def test_rectangle_perimeter_yes(self):  # Тестирование корректного расчета периметра прямоугольника
        res = rectangle.perimeter(4, 7)  # Вычисление периметра с длиной 4 и шириной 7
        self.assertEqual(res, 22)  # Проверка результата

    def test_rectangle_perimeter_no(self):  # Тестирование поведения при отрицательной ширине
        res = rectangle.perimeter(4, -7)  # Вычисление периметра с отрицательной шириной
        self.assertEqual(res, -6)  # Проверка, что результат соответствует ожидаемому (некорректное поведение)

    def test_rectangle_perimeter_real_numbers(self):  # Тестирование периметра с вещественными числами
        res = rectangle.perimeter(4.25, 7.36)  # Вычисление периметра с длиной 4.25 и шириной 7.36
        self.assertEqual(res, 23.22)  # Проверка на равенство ожидаемому значению

    def test_rectangle_perimeter_zero(self):  # Тестирование периметра с одной стороной равной нулю
        res = rectangle.perimeter(4, 0)  # Вычисление периметра при ширине 0
        self.assertEqual(res, 8)  # Проверка результата

if __name__ == "__main__":  # Проверка, что скрипт запущен напрямую
    unittest.main()  # Запуск всех тестов
rect_tests = RectangleTestCase  # Создание экземпляра тестов для импортирования в файл с функцией