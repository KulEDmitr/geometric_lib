import unittest
import square

class SquareTestCase(unittest.TestCase):
    # Проверяет, когда сторона равна 0
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    # Проверяет, когда сторона равна 10
    def test_area_positive(self):
        self.assertEqual(square.area(10), 100)

    # Проверяет, является ли сторона действительным числом
    def test_area_float(self):
        self.assertEqual(square.area(8.5), 72.25)

    # Проверяет, когда периметр равен 0
    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    # Проверяет, когда сторона равна 10
    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(10), 40)

    # Проверяет, является ли сторона действительным числом
    def test_perimeter_float(self):
        self.assertEqual(square.perimeter(17.25), 69)

    # Проверяет правильное значение для площади
    def test_area_incorrect_value(self):
        self.assertNotEqual(square.area(10), 40)

    # Проверяет правильное значение для периметра
    def test_perimeter_incorrect_value(self):
        self.assertNotEqual(square.perimeter(10), 30)

    # Проверяет площадь квадрата, когда сторона отрицательная
    def test_area_negative(self):
        self.assertEqual(square.area(-5), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона отрицательная
    def test_perimeter_negative(self):
        self.assertEqual(square.perimeter(-5), "Incorrect input")

    # Проверяет площадь квадрата, когда сторона является символом
    def test_area_char_input(self):
        self.assertEqual(square.area('a'), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона является символом
    def test_perimeter_char_input(self):
        self.assertEqual(square.perimeter('a'), "Incorrect input")

    # Проверяет площадь квадрата, когда сторона является строкой
    def test_area_string_input(self):
        self.assertEqual(square.area("string"), "Incorrect input")

    # Проверяет периметр квадрата, когда сторона является строкой
    def test_perimeter_string_input(self):
        self.assertEqual(square.perimeter("string"), "Incorrect input")

    # Проверяет, когда сторона слишком большим числом
    def test_area_large_integer(self):
        self.assertEqual(square.area(100000000000000000000), "Incorrect input")

    # Проверяет, когда сторона слишком большим числом
    def test_perimeter_large_integer(self):
        self.assertEqual(square.perimeter(100000000000000000000), "Incorrect input")

if __name__ == '__main__':
    unittest.main()