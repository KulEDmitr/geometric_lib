import math
import unittest
class RectangleTestCase(unittest.TestCase):
    def test_0_area(self):
       res = area(0)
       self.assertEqual(res, 0)

    def test_1_area(self):
        res = area(100_000)
        self.assertEqual(res,math.pi*100_000*100_000)
    @unittest.expectedFailure
    def test_2_area(self):
        res = area('a')
        self.assertEqual(res,TypeError)

    def test_0_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_1_perimeter(self):
        res = perimeter(100_000)
        self.assertEqual(res,2*math.pi*100_000)
    @unittest.expectedFailure
    def test_2_perimeter(self):
        res = perimeter('a')
        self.assertEqual(res,TypeError)

def area(r):
    '''Принимает радиус круга, возвращает площадь круга. Пример вызова функции: area(3) -> 28.274333882308138'''
    return math.pi * r * r

def perimeter(r):
    '''
        Принимает радиус круга, возвращает длину окружности круга. Пример вызова функции: perimeter(3) -> 18.84955592153876
    '''
    return 2 * math.pi * r

print(perimeter(100000))

