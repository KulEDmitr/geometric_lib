import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны положительные
    def test_area_positive(self):
        self.assertEqual(triangle.area(7, 8), 28)

    # Проверяет, когда стороны равны 10
    def test_area_base_height_ten(self):
        self.assertEqual(triangle.area(10, 10), 50)

    # Проверяет, являются ли стороны действительным числом
    def test_area_float(self):
        self.assertEqual(triangle.area(7.5, 3.5), 13.125)

    # Проверяет, когда периметр равен 0
    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    # Проверяет, когда стороны равны 10
    def test_perimeter_positive(self):
        self.assertEqual(triangle.perimeter(10, 6, 8), 24)

    # Проверяет, являются ли стороны действительным числом
    def test_perimeter_float(self):
        self.assertEqual(triangle.perimeter(34.23, 42.34, 23.43), 100)

    # Проверяет правильное значение для площади
    def test_area_incorrect_value(self):
        self.assertNotEqual(triangle.area(10, 10), 40)

    # Проверяет правильное значение для периметра
    def test_perimeter_incorrect_value(self):
        self.assertNotEqual(triangle.perimeter(10, 6, 8), 30)

    # Проверяет площадь треугольника, когда стороны отрицательные
    def test_area_negative(self):
        self.assertEqual(triangle.area(-5, 10), "Incorrect input")

    # Проверяет периметр треугольника, когда стороны отрицательные
    def test_perimeter_negative(self):
        self.assertEqual(triangle.perimeter(-5, 10, 15), "Incorrect input")

    # Проверяет площадь квадрата, когда сторона является символом
    def test_area_char_input(self):
        self.assertEqual(triangle.area('a', 3), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона является символом
    def test_perimeter_char_input(self):
        self.assertEqual(triangle.perimeter('a', 3, 4), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона является символом
    def test_area_string_input(self):
        self.assertEqual(triangle.area(4, "abcdef"), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона является символом
    def test_perimeter_string_input(self):
        self.assertEqual(triangle.perimeter(4, "abcdef", 5), "Incorrect input")

    # Проверяет, когда сторона слишком большим числом
    def test_area_large_integer(self):
        self.assertEqual(triangle.area(10**15, 3), "Incorrect input")

    # Проверяет, когда сторона слишком большим числом
    def test_perimeter_large_integer(self):
        self.assertEqual(triangle.perimeter(10**15, 3, 4), "Incorrect input")

if __name__ == '__main__':
    unittest.main()