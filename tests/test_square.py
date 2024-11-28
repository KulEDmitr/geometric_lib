import unittest
from square import area_square
from square import perimeter_square

class SquareTestCase(unittest.TestCase):
    # Проверяет, когда сторона равна 0
    def test_0_mul(self):
        result = area_square(0)
        self.assertEqual(result, 0)
    # Проверяет, когда сторона равна 10
    def test_1_mul(self):
        result = area_square(10)
        self.assertEqual(result, 100)
    # Проверяет, когда сторона равна 7,5
    def test_2_mul(self):
        result = area_square(7.5)
        self.assertEqual(result, 56.25)
    # Проверяет, когда сторона равна 56,25
    def test_3_mul(self):
        result = perimeter_square(0)
        self.assertEqual(result, 0)
    # Проверяет, когда сторона равна 10
    def test_4_mul(self):
        result = perimeter_square(10)
        self.assertEqual(result, 40)
    # Проверяет, когда сторона равна 17,25
    def test_5_mul(self):
        result = perimeter_square(17.25)
        self.assertEqual(result, 69)

    

if __name__ == '__main__':
    unittest.main()