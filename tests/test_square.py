import square
import unittest

class SquareTestCase(unittest.TestCase):
    # Проверяет, когда сторона равна 0
    def test_zero_mul(self):
        self.assertEqual(square.area(0), 0)

    # Проверяет, когда сторона равна 10
    def test_one_mul(self):
        self.assertEqual(square.area(10), 100)

    # Проверяет, является ли сторона действительным числом
    def test_two_mul(self):
        self.assertEqual(square.area(8.5), 72.25)

    # Проверяет, когда периметр равен 0
    def test_three_mul(self):
        self.assertEqual(square.perimeter(0), 0)

    # Проверяет, когда сторона равна 10
    def test_four_mul(self):
        self.assertEqual(square.perimeter(10), 40)

    # Проверяет, является ли сторона действительным числом
    def test_five_mul(self):
        self.assertEqual(square.perimeter(2.25), 9)

    # Проверяет правильное значение для площади
    def test_six_mul(self):
        self.assertNotEqual(square.area(10), 40)

    # Проверяет правильное значение для периметра
    def test_seven_mul(self):
        self.assertNotEqual(square.perimeter(10), 30)

    # Проверяет площадь квадрата, когда сторона отрицательная
    def test_eight_mul(self):
        self.assertEqual(square.area(-5), "wrong input")
        
    def test_nine_mul(self):
        self.assertEqual(square.perimeter(-5), "wrong input")

    # Проверяет площадь квадрата, когда сторона является символом
    def test_ten_mul(self):
        self.assertEqual(square.area('a'), "wrong input")

    def test_eleven_mul(self):
        self.assertEqual(square.perimeter('a'), "wrong input")

    # Проверяет площадь квадрата, когда сторона является строкой
    def test_twelve_mul(self):
        self.assertEqual(square.area("string"), "wrong input")

    def test_thirteen_mul(self):
        self.assertEqual(square.perimeter("string"), "wrong input")

    # Проверяет, когда сторона слишком большим числом
    def test_fourteen_mul(self):
        self.assertEqual(square.area(100000000000000000000), "wrong input")

    def test_fiveteen_mul(self):
        self.assertEqual(square.perimeter(100000000000000000000), "wrong input")

if __name__ == '__main__':
    unittest.main()