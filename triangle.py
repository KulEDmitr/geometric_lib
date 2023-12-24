import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_perim_13_12_5(self):
        res = perimeter(13, 12, 5)
        self.assertEqual(res, 30)
    
    def test_perim_1_1_1(self):
        res = perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perim_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

def area(a, h): 
    '''
        Возвращает площадь треугольника.

            Параметры:
                a (int): длина стороны, на которую опущена высота
                h (int): длина высоты

            Возвращаемое значение: 
                a * h / 2 (double): полупроизведение высоты и данной стороны
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
        Возвращает периметр треугольника.

            Параметры:
                a (int): длина стороны 1
                b (int): длина стороны 2
                c (int): длина стороны 3

            Возвращаемое значение: 
                a + b + c: сумма трех сторон треугольника
    '''
    return a + b + c 
