import unittest
from rectangle import area_rectangle
from rectangle import perimeter_rectangle

class RectangleTestCase(unittest.TestCase):
    # Проверяет, когда стороны равны 0, 10
    def test_0_mul(self):
        result = area_rectangle(0,13)
        self.assertEqual(result, 0)
    # Проверяет, когда стороны равны 10, 13
    def test_1_mul(self):
        result = area_rectangle(10,13)
        self.assertEqual(result, 130)
    # Проверяет, когда стороны равны 67,5, 3,5
    def test_2_mul(self):
        result = area_rectangle(67.5,3.5)
        self.assertEqual(result, 236.25)
    # Проверяет, когда стороны равны 0,0
    def test_3_mul(self):
        result = perimeter_rectangle(0,0)
        self.assertEqual(result, 0)
    # Проверяет, когда стороны равны 10,54
    def test_4_mul(self):
        result = perimeter_rectangle(10,54)
        self.assertEqual(result, 128)
    # Проверяет, когда стороны равны -6,5
    def test_5_mul(self):
        result = perimeter_rectangle(-6,5)
        self.assertEqual(result, "Incorrect input" )
    
if __name__ == '__main__':
    unittest.main()
    

    