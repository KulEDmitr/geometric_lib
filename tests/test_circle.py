import circle
import unittest

class CircleTestCase(unittest.TestCase):
    # Проверяет, когда радиус равен 0
    def test_zero_mul(self):
        assert circle.area(0) == 0

    # Проверяет, когда радиус равен 10
    def test_one_mul(self):
        assert circle.area(10) == 314.1592653589793

    # Проверяет, является ли радиус действительным числом
    def test_two_mul(self):
        assert circle.area(67.636) == 14371.619275936122

    # Проверяет, когда окружность с радиусом равна 0
    def test_three_mul(self):
        assert circle.perimeter(0) == 0

    # Проверяет, когда окружность равен 10
    def test_four_mul(self):
        assert circle.perimeter(10) == 62.83185307179586

    # Проверяет, является ли окружность действительным числом
    def test_five_mul(self):
        assert circle.perimeter(67.636) == 424.96952143639845

    # Проверяет, когда радиус отрицательный
    def test_six_mul(self):
        assert circle.area(10) != 40

    # Проверяет, когда окружность отрицательный
    def test_seven_mul(self):
        assert circle.perimeter(10) != 30

    # когда есть отрицательный фронт
    def test_eight_mul(self):
        res = circle.area(-10)
        self.assertEqual(res, "wrong input")

    def test_nine_mul(self):
        res = circle.perimeter(-10)
        self.assertEqual(res, "wrong input")

    # Проверяет, являются ли радиус символами
    def test_ten_mul(self):
        res = circle.area('a')
        self.assertEqual(res, "wrong input")

    def test_eleven_mul(self):
        res = circle.perimeter('a')
        self.assertEqual(res, "wrong input")

    # Проверяет, являются ли радиус строкой
    def test_twelve_mul(self):
        res = circle.area('abcdef')
        self.assertEqual(res, "wrong input")

    def test_thirteen_mul(self):
        res = circle.perimeter('abcdef')
        self.assertEqual(res, "wrong input")

    # Проверяет, является ли радиус слишком большим числом
    def test_fourteen_mul(self):
        res = circle.area(10000000000000000000000000)
        self.assertEqual(res, "wrong input")

    def test_fiveteen_mul(self):
        res = circle.perimeter(10000000000000000000000000)
        self.assertEqual(res, "wrong input")

if __name__ == '__main__':
    unittest.main()

