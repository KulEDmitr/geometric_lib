import unittest

def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)

class RectangleTestCase(unittest.TestCase):
    # Функция test_zero_mul проверяет, что площадь равна нулю, если один из параметров равен нулю.
    def test_zero_mul(self):
        res = area(10, 0)  # вызываем функцию с параметрами (10, 0)
        self.assertEqual(res, 0)  # проверяем, что результат равен 0

    # Функция test_square_mul проверяет, что площадь рассчитывается правильно для квадрата.
    def test_square_mul(self):
        res = area(10, 10)  # вызываем функцию с параметрами (10, 10)
        self.assertEqual(res, 100)  # проверяем, что результат равен 100
