import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_perim_5_13(self):
        res = perimeter(5, 13)
        self.assertEqual(res, 36)
    
    def test_perim_5_5(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_perim_5_0(self):
        res = perimeter(5, 0)
        self.assertEqual(res, 10)

    def test_perim_5_1(self):
        res = perimeter(5, 1)
        self.assertEqual(res, 12)

    def test_square_mul_1(self):
        res = area(14, 1)
        self.assertEqual(res, 14)

def area(a, b): 
    '''
        Возвращает площадь прямоугольника.

            Параметры: 
                a (int): длина первой из сторон прямоугольника
                b (int): длина второй из сторон прямоугольника

            Возвращаемое значение: 
                a * b (int): произведение чисел a и b
    '''
    return a * b 

def perimeter(a, b): 
    '''
        Возвращает периметр прямоугольника.

            Параметры: 
                a (int): длина первой из сторон прямоугольника
                b (int): длина второй из сторон прямоугольника

            Возвращаемое значение: 
                2 * (a + b) (int): удвоенная сумма чисел a и b
    '''
    return 2 * (a + b) 
