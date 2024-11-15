import unittest
import circle

class CircleTestCase(unittest.TestCase):
    # Проверяет, когда радиус равен 0
    def test_area_zero_radius(self):
        assert circle.area(0) == 0

    # Проверяет, когда радиус равен 10
    def test_area_positive_radius(self):
        assert circle.area(10) == 314.1592653589793

    # Проверяет, является ли радиус действительным числом
    def test_area_float_radius(self):
        assert circle.area(67.636) == 14371.619275936122

    # Проверяет, когда окружность с радиусом равна 0
    def test_perimeter_zero_radius(self):
        assert circle.perimeter(0) == 0

    # Проверяет, когда окружность равен 10
    def test_perimeter_positive_radius(self):
        assert circle.perimeter(10) == 62.83185307179586

    # Проверяет, является ли окружность действительным числом
    def test_perimeter_float_radius(self):
        assert circle.perimeter(67.636) == 424.96952143639845

    # Проверяет, когда радиус отрицательный
    def test_area_incorrect_value(self):
        assert circle.area(10) != 40

    # Проверяет, когда окружность отрицательный
    def test_perimeter_incorrect_value(self):
        assert circle.perimeter(10) != 30

    # Проверяет, когда радиус отрицательный
    def test_area_negative_radius(self):
        res = circle.area(-10)
        self.assertEqual(res, "Incorrect input")

    # Проверяет, когда окружность отрицательный
    def test_perimeter_negative_radius(self):
        res = circle.perimeter(-10)
        self.assertEqual(res, "Incorrect input")

    # Проверяет, являются ли радиус символами
    def test_area_char_input(self):
        res = circle.area('a')
        self.assertEqual(res, "Incorrect input")

    # Проверяет, являются ли окружность символами
    def test_perimeter_char_input(self):
        res = circle.perimeter('a')
        self.assertEqual(res, "Incorrect input")

    # Проверяет, являются ли радиус строкой
    def test_area_string_input(self):
        res = circle.area('abcdef')
        self.assertEqual(res, "Incorrect input")

    # Проверяет, являются ли окружность строкой
    def test_perimeter_string_input(self):
        res = circle.perimeter('abcdef')
        self.assertEqual(res, "Incorrect input")
        
    # Проверяет, является ли радиус слишком большим числом
    def test_area_large_integer(self):
        res = circle.area(10000000000000000000000000)
        self.assertEqual(res, "Incorrect input")

    # Проверяет, является ли окружность слишком большим числом
    def test_perimeter_large_integer(self):
        res = circle.perimeter(10000000000000000000000000)
        self.assertEqual(res, "Incorrect input")

if __name__ == '__main__':
    unittest.main()