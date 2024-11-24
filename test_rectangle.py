import rectangle
import unittest

class RectangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны равны 0
    def test_zero_mul(self):
        assert rectangle.area(0,15) == 0
    # Проверяет, когда стороны равны 10
    def test_one_mul(self):
        assert rectangle.area(10,10) == 100
    # Проверяет, являются ли стороны действительным числом
    def test_two_mul(self):
        assert rectangle.area(65.5, 4.5) == 294.75
    # Проверяет, когда периметр равен 0
    def test_three_mul(self):
        assert rectangle.perimeter(0,0) == 0
    # Проверяет, когда стороны равны 10
    def test_four_mul(self):
        assert rectangle.perimeter(10, 45) == 110
    # Проверяет, являются ли стороны действительным числом
    def test_five_mul(self):
        assert rectangle.perimeter(67.636, 42.364) == 220

    # Проверяет правильное значение для площади
    def test_six_mul(self):
        assert rectangle.area(7,8) != 55

    # Проверяет правильное значение для периметра
    def test_seven_mul(self):
        assert rectangle.perimeter(10, 54) != 132

    # когда есть отрицательный фронт
    def test_eight_mul(self):
        self.assertEqual(rectangle.area(-8, 7), "wrong input")

    def test_nine_mul(self):
        self.assertEqual(rectangle.perimeter(-5, 4), "wrong input")

    # когда есть ребро, которое является символом
    def test_ten_mul(self):
        self.assertEqual(rectangle.area('n', 8), "wrong input")

    def test_eleven_mul(self):
        self.assertEqual(rectangle.perimeter('n', 8), "wrong input")

    # когда есть край, представляющий строку
    def test_twelve_mul(self):
        self.assertEqual(rectangle.area('abcdef', 12), "wrong input")

    def test_thirteen_mul(self):
        self.assertEqual(rectangle.perimeter('abcdef', 12), "wrong input")

    # когда стороны слишком большим числом
    def test_fourteen_mul(self):
        self.assertEqual(rectangle.area(10000000000000000000000000, 9), "wrong input")

    def test_fiveteen_mul(self):
        self.assertEqual(rectangle.perimeter(10000000000000000000000000, 9), "wrong input")
