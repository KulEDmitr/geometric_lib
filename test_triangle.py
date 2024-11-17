import unittest
from triangle import area_triangle
from triangle import perimeter_triangle

class TriangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны равны 7,8,
    def test_0_mul(self):
        result = area_triangle(7, 8)
        self.assertEqual(result, 28)
    # Проверяет, когда стороны равны 10,5
    def test_1_mul(self):
        result = area_triangle(10, 5)
        self.assertEqual(result, 25)
    # Проверяет, когда стороны равны 7.5 3.5
    def test_2_mul(self):
        result = area_triangle(7.5, 3.5)
        self.assertEqual(result, 4)
    # Проверяет, когда стороны равны 0 0 0
    def test_3_mul(self):
        result = perimeter_triangle(0, 0,0)
        self.assertEqual(result, 0)
    # Проверяет, когда стороны равны 10, 4, 8
    def test_4_mul(self):
        result = perimeter_triangle(10, 4, 8)
        self.assertEqual(result, 22)
    # Проверяет, когда стороны равны 34.23, 42.34, 23.43
    def test_5_mul(self):
        result = perimeter_triangle(34.23, 42.34, 23.43)
        self.assertEqual(result, 100)
    
if __name__ == '__main__':
    unittest.main()