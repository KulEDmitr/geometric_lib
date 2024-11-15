import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны равны 0
    def test_area_zero_side(self):
        assert rectangle.area(0,13) == 0
    # Проверяет, когда стороны равны 10
    def test_area_positive_sides(self):
        assert rectangle.area(10,10) == 100
    # Проверяет, являются ли стороны действительным числом
    def test_area_float_sides(self):
        assert rectangle.area(65.5, 4.5) == 294.75
    # Проверяет, когда периметр равен 0
    def test_perimeter_zero_sides(self):
        assert rectangle.perimeter(0,0) == 0
    # Проверяет, когда стороны равны 10
    def test_perimeter_positive_sides(self):
        assert rectangle.perimeter(10, 54) == 128
    # Проверяет, являются ли стороны действительным числом
    def test_perimeter_float_sides(self):
        assert rectangle.perimeter(67.636, 42.364) == 220

    # Проверяет правильное значение для площади
    def test_area_incorrect_value(self):
        assert rectangle.area(7,8) != 50

    # Проверяет правильное значение для периметра
    def test_perimeter_incorrect_value(self):
        assert rectangle.perimeter(10, 54) != 120

    # Проверяет площадь прямоугольника, когда стороны отрицательные
    def test_area_negative_sides(self):
        self.assertEqual(rectangle.area(-5, 4), "Incorrect input")

    # Проверяет периметр прямоугольника, когда стороны отрицательные
    def test_perimeter_negative_sides(self):
        self.assertEqual(rectangle.perimeter(-5, 4), "Incorrect input")

    # Проверяет периметр прямоугольника, когда стороны являются символами
    def test_area_char_input(self):
        self.assertEqual(rectangle.area('a', 4), "Incorrect input")

    # Проверяет периметр прямоугольника, когда стороны являются символами
    def test_perimeter_char_input(self):
        self.assertEqual(rectangle.perimeter('a', 4), "Incorrect input")

    # Проверяет периметр прямоугольника, когда стороны являются строками
    def test_area_string_input(self):
        self.assertEqual(rectangle.area('abcdef', 4), "Incorrect input")

    # Проверяет периметр прямоугольника, когда стороны являются строками
    def test_perimeter_string_input(self):
        self.assertEqual(rectangle.perimeter('abcdef', 4), "Incorrect input")

    # Проверяет, когда стороны слишком большим числом
    def test_area_large_integer(self):
        self.assertEqual(rectangle.area(10000000000000000000000000, 4), "Incorrect input")

    # Проверяет, когда стороны слишком большим числом
    def test_perimeter_large_integer(self):
        self.assertEqual(rectangle.perimeter(10000000000000000000000000, 4), "Incorrect input")

if __name__ == '__main__':
    unittest.main()