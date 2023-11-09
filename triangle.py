import unittest
class RectangleTestCase(unittest.TestCase):
    def test_1_area(self):
        res = area(2,0)
        self.assertEqual(res,0)
    
    def test_2_area(self):
        res = area(100_000_000,100_000_000)
        self.assertEqual(res,100_000_000*100_000_000/2)

    @unittest.expectedFailure
    def test_3_area(self):
        res = area('a',2)
        self.assertEqual(res)
    
    @unittest.expectedFailure
    def test_4_area(self):
        res = area('a','b')
        self.assertEqual(res)

    def test_0_perimeter(self):
        res = perimeter(0,0,0)
        self.assertEqual(res,0)
    
    def test_1_perimeter(self):
        res = perimeter(1000,1000_000,213)
        self.assertEqual(res,1000+1000_000+213)

    def test_2_perimeter(self):
        res = perimeter('a','b','c')
        self.assertEqual(res,TypeError)

    @unittest.expectedFailure
    def test_3_perimeter(self):
        res = perimeter('a','b',3)
        self.assertEqual(res)
        



def area(a, h): 
    '''Принимает число сторону и высоту треугольника проведённую к этой стороне, возвращает площадь треугольника. Пример вызова: area(2,2) -> 2'''
    return a * h / 2 

def perimeter(a, b, c):
    '''Принимает три строны треугольника, возвращает периметр. Пример вызова: perimeter(2,2,2) -> 6''' 
    return a + b + c 
print(100_000_000*100_000_000/2)