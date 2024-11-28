import unittest
from circle import area_circle
from circle import perimeter_circle

class CircleTestCase(unittest.TestCase):
     # Проверяет, когда радиус равен 0
    def test_0_mul(self):
        result = area_circle(0)
        self.assertEqual(result, 0)
     # Проверяет, когда радиус равен 10
    def test_1_mul(self):
        result = area_circle(10)
        self.assertEqual(result, 314.1592653589793)
     # Проверяет, когда радиус равен 67.636
    def test_2_mul(self):
        result = area_circle(67.636)
        self.assertEqual(result, 14371.619275936122)
     # Проверяет, когда радиус равен 5
    def test_3_mul(self):
        result = perimeter_circle(5)
        self.assertEqual(result, 31.41592653589793 )
     # Проверяет, когда радиус равен 10
    def test_4_mul(self):
        result = perimeter_circle(10)
        self.assertEqual(result, 62.83185307179586)
     # Проверяет, когда радиус равен -10
    def test_5_mul(self):
        result = perimeter_circle(-10)
        self.assertEqual(result, "Incorrect input")

if __name__ == '__main__':
    unittest.main()