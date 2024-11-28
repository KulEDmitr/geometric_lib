import unittest  # Импортирование модуля для юнит-тестирования
import square  # Импортирование модуля с функциями для вычисления площади и периметра квадрата

class SquareTestCase(unittest.TestCase):  # Определение класса для тестирования квадрата

    def test_square_area_ex(self):  # Тестирование корректного расчета площади квадрата
        rst = square.area(5)  # Вычисление площади квадрата со стороной 5
        self.assertEqual(rst, 25)  # Проверка, что результат равен ожидаемому значению 25

    def test_square_area_neg(self):  # Тестирование поведения при отрицательной стороне квадрата
        res = square.area(-5)  # Вычисление площади квадрата со стороной -5
        self.assertEqual(res, 25)  # Проверка, что результат (некорректное поведение) равен 25

    def test_square_area_float_num(self):  # Тестирование площади с вещественным числом
        res = square.area(2.56)  # Вычисление площади квадрата со стороной 2.56
        self.assertEqual(res, 6.5536)  # Проверка на соответствие с ожидаемым результатом

    def test_square_area_zero(self):  # Тестирование площади с нулевой стороной
        res = square.area(0)  # Вычисление площади квадрата со стороной 0
        self.assertEqual(res, 0)  # Проверка, что площадь равна 0

    def test_square_perimeter_ex(self):  # Тестирование корректного расчета периметра квадрата
        res = square.perimeter(4)  # Вычисление периметра квадрата со стороной 4
        self.assertEqual(res, 16)  # Проверка результата

    def test_square_perimeter_no(self):  # Тестирование поведения при отрицательной стороне квадрата
        res = square.perimeter(-3)  # Вычисление периметра квадрата со стороной -3
        self.assertEqual(res, -12)  # Проверка, что результат (некорректное поведение) равен -12

    def test_square_perimeter_float_num(self):  # Тестирование периметра с вещественным числом
        res = square.perimeter(4.12)  # Вычисление периметра квадрата со стороной 4.12
        self.assertEqual(res, 16.48)  # Проверка на соответствие результату

    def test_square_perimeter_zero(self):  # Тестирование периметра с нулевой стороной
        res = square.perimeter(0)  # Вычисление периметра квадрата со стороной 0
        self.assertEqual(res, 0)  # Проверка, что периметр равен 0

if __name__ == '__main__':  # Проверка, что скрипт запущен напрямую
    unittest.main()  # Запуск всех тестов
squar_tests = SquareTestCase  # Создание экземпляра тестов 