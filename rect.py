import unittest

def area(a, b):
	return a * b
	'''
       Вычисляет площадь прямоугольника.

       Параметры:
       a (float): Длина прямоугольника.
	   b (float): Ширина прямоугольника.
                
       Возвращаемое значение:
       float: Площадь прямоугольника.

       Исключения: Отсутствуют.  

       Пример:
       >>> area(10, 5)
       50
    '''

def perimeter(a, b):
	return 2 * (a + b)	
	'''
       Вычисляет периметр прямоугольника.

       Параметры:
       a (float): Длина прямоугольника.
	   b (float): Ширина прямоугольника.
                
       Возвращаемое значение:
       float: Периметр прямоугольника.

       Исключения: Отсутствуют.  

       Пример:
       >>> perimeter(10, 5)
       30
    '''

class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10, 25)
        self.assertEqual(res, 250)
        
    def test_perimeter(self):
        res = perimeter(10, 25)
        self.assertEqual(res, 70)
        