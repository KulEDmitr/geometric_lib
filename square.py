import unittest

def area(a):
    return a * a
    '''
       Вычисляет площадь квадрата.

       Параметры:
       a (float): Длина квадрата.
                
       Возвращаемое значение:
       float: Площадь квадрата.

       Исключения: Отсутствуют.  

       Пример:
       >>> area(10)
       100
    '''
            
def perimeter(a):
    return 4 * a
    '''
       Вычисляет периметр квадрата.

       Параметры:
       a (float): Длина квадрата.
                
       Возвращаемое значение:
       float: периметр квадрата.

       Исключения: Отсутствуют.  

       Пример:
       >>> perimeter(10)
       40
    '''

class SquareTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10)
        self.assertEqual(res, 100)
        

    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
