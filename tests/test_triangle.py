import triangle
import unittest

class TriangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны равны 0
    def test_zero_mul(self):
        self.assertEqual(triangle.area(7, 8), 28)

    # Проверяет, когда стороны равны 10
    def test_one_mul(self):
        self.assertEqual(triangle.area(10, 10), 50)

    # Проверяет, являются ли стороны действительным числом
    def test_two_mul(self):
        self.assertEqual(triangle.area(7.5, 3.5), 13.125)

    # Проверяет, когда периметр равен 0
    def test_three_mul(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    # Проверяет, когда стороны равны 10
    def test_four_mul(self):
        self.assertEqual(triangle.perimeter(10, 6, 8), 24)

    # Проверяет, являются ли стороны действительным числом
    def test_five_mul(self):
        self.assertEqual(triangle.perimeter(34.23, 42.34, 23.43), 100)

    # Проверяет правильное значение для площади
    def test_six_mul(self):
        self.assertNotEqual(triangle.area(10, 10), 40)

    # Проверяет правильное значение для периметра
    def test_seven_mul(self):
        self.assertNotEqual(triangle.perimeter(10, 6, 8), 30)

    # Проверяет площадь треугольника, когда стороны отрицательные
    def test_eight_mul(self):
        self.assertEqual(triangle.area(-5, 10), "wrong input")

    def test_nine_mul(self):
        self.assertEqual(triangle.perimeter(-5, 10, 15), "wrong input")

    # Проверяет площадь квадрата, когда сторона является символом
    def test_ten_mul(self):
        self.assertEqual(triangle.area('a', 3), "wrong input")

    def test_eleven_mul(self):
        self.assertEqual(triangle.perimeter('a', 3, 4), "wrong input")

    # Проверяет периметр квадрата, когда сторона является символом
    def test_twelve_mul(self):
        self.assertEqual(triangle.area(4, "string"), "wrong input")

    def test_thirteen_mul(self):
        self.assertEqual(triangle.perimeter(4, "string", 5), "wrong input")

    # Проверяет, когда сторона слишком большим числом
    def test_fourteen_mul(self):
        self.assertEqual(triangle.area(10**15, 3), "wrong input")

    def test_fiveteen_mul(self):
        self.assertEqual(triangle.perimeter(10**15, 3, 4), "wrong input")

if __name__ == '__main__':
    unittest.main()