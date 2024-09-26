import unittest

class TriangleTestCase(unittest.TestCase):

    def test_zero_value_area(self):
        result = area(0, 0)
        self.assertEqual(result, 0, "Incorrect on zero side and height in area in triangle.")

    def test_integer_value_area(self):
        result = area(5, 6)
        self.assertEqual(result, 15, "Incorrect on integer side and height in area in triangle.")

    def test_float_value_area(self):
        result = area(2.5, 2.6)
        self.assertEqual(result, 3.25, "Incorrect on float side and height in area in triangle.")

    def test_string_value_area(self):
        try:
            result = area("a", "b")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in triangle.")

    def test_one_string_value_area(self):
        try:
            result = area(6, "a")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in area in triangle.")

    def test_zero_value_perimeter(self):
        result = perimeter(0, 0, 0)
        self.assertEqual(result, 0, "Incorrect on zero all side in perimeter in triangle.")

    def test_integer_value_perimeter(self):
        result = perimeter(5, 6, 7)
        self.assertEqual(result, 18, "Incorrect on simple all side in perimeter in triangle.")

    def test_float_value_perimeter(self):
        result = perimeter(5.5, 6.5, 7.5)
        self.assertEqual(result, 19.5, "Incorrect on float all side in perimeter in triangle.")

    def test_string_value_perimeter(self):
        try:
            result = perimeter("a", "b", "c")
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeters in triangle.")

    def test_one_string_value_perimeter(self):
        try:
            result = perimeter("a", 2, 3)
        except Exception as error:
            result = error.__class__
        self.assertEqual(result, TypeError, "Incorrect catch exceptions in perimeters in triangle.")

def area(a, h):
    '''
    Возвращает площадь заданого треугольника
	
	Параметры:
	    a (int): длина стороны треугольника, к которой проведена высота
	    h (int): высота треугольника

	Возвращаемое значение:
	    area (float): площадь искомого треугольника

    Пример вызова:
        triangle_area = area(5, 10)
    Результат:
        triangle_area = 25.0
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Возвращает периметр заданого треугольника
	
	Параметры:
	    a (int): длина первой стороны треугольника
	    b (int): длина второй стороны треугольника
	    c (int): длина третей стороны треугольника

	Возвращаемое значение:
	    perimeter (int): периметр искомого треугольника

    Пример вызова:
        triangle_perimeter = perimeter(5, 10, 6)
    Результат:
        triangle_perimeter = 21
    '''
    return a + b + c
