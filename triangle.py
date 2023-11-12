import unittest
def area(a, h):
    '''
    
    Функция принимает два натуральных десятичных числа (a,h) и возвращает десятичное число, равное площади треугольника, у которого число a - величина стороны, h - длина перпендикуляра опущенного из противоположной вершины к данной стороне.
    Пример: area(10, 5) = 25
    
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    
    Функция принимает три натуральных десятичных числа и возвращает десятичное натуральное число, равное периметру треугольника, длины сторон которого соотвественно равны данным числам.
    Пример: perimeter(10, 20, 5) = 35
    
    '''
    return a + b + c 
class TriangleTestCase(unittest.TestCase):
    def test_zero_side(self):
        with self.assertRaises(ValueError):
            area(0,10)
    def test_zero_height(self):
        with self.assertRaises(ValueError):
            area(10,0)
    def test_zero_sides(self):
        with self.assertRaises(ValueError):
            perimeter(0,5,3)
            perimeter(5,0,1)
            perimeter(4,1,0)
    def test_random(self):
        self.assertEqual(area(64,3), 96)
        self.assertEqual(area(1,1), 1/2)
        self.assertEqual(perimeter(298,3,1), 302)
        self.assertEqual(perimeter(87,45,56),188)
    def test_float(self):
        self.assertEqual(area(1, 0.3), 0.3/2)
        self.assertEqual(perimeter(0.3,0.4,0.2), 0.3+0.4+0.2)
    def test_wrong_value(self):
        with self.assertRaises(TypeError):
            area('dkkd',2)
        with self.assertRaises(TypeError):
            perimeter('dkkd', 3, 2)
    def test_negative_value(self):
        with self.assertRaises(ValueError):
            area(-20,2)
            area(4,-20)
        with self.assertRaises(ValueError):
            perimeter(-400,8,2)
            perimeter(9,-98,7)
            perimeter(76,78,-8)