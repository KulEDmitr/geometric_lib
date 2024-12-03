import unittest

def area(a, h):
	return a * h / 2
	'''
       Вычисляет площадь прямоугольника.

       Параметры:
       a (float): Основание треугольника.
	   h (float): Высота треугольника.
                
       Возвращаемое значение:
       float: Площадь треугольника.

       Исключения: Отсутствуют.  

       Пример:
       >>> area(10, 5)
       25
    '''

def perimeter(a, b, c):
	return a + b + c
	'''
       Вычисляет периметр прямоугольника.

       Параметры:
       a (float): сторона треугольника.
	   b (float): сторона треугольника.
       c (float): сторона треугольника.

                
       Возвращаемое значение:
       float: Периметр треугольника.

       Исключения: Отсутствуют.  

       Пример:
       >>> perimeter(10, 5, 6)
       21
    '''
      
class TriangleTestCase(unittest.TestCase):

    def test_area(self):
        res = area(10, 4)
        self.assertEqual(res, 20)
        

    def test_perimeter(self):
        res = perimeter(10, 30, 45)
        self.assertEqual(res, 85)
