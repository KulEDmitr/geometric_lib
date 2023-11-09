import unittest
class RectangleTestCase(unittest.TestCase):
    def test_0_area(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_1_area(self):
       res = area(10)
       self.assertEqual(res, 100)
    
    def test_2_area_(self):
       res = area(200_000_000_000_000_000)
       self.assertEqual(res,200_000_000_000_000_000*200_000_000_000_000_000)

    @unittest.expectedFailure
    def test_wrong_input_1_area(self):
       res = area('b')
       self.assertEqual(res)
    
    def test_0_perimeter(self):
       res = perimeter(0)
       self.assertEqual(res,0)

    def test_1_perimeter(self):
       res = perimeter(10)
       self.assertEqual(res,40) 

    def test_2_perimeter(self):
       res = perimeter(100000)
       self.assertEqual(res,4*100000)

    
    @unittest.expectedFailure
    def test_3_perimeter_wrong_input(self):
       res = perimeter("a")
       self.assertEqual(res)
    



def area(a):
    '''Принимает число n, возвращает квадрат числа n. Пример вызова функции area(5) -> 25'''
    return a * a

def perimeter(a):
    '''Принимает сторону квадратна, возвращает периметр квадрата. Пример вызова функции: perimeter(4) -> 16'''
    return 4 * a  