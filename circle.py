from math import pi
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = area(0)
        self.assertEqual(res, 0, "Incorrect on zero radius in area in circle.")

    def test_string_value_area(self):
        try:
            res = area("abc")
        except Exception as error:
            res = error.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in area in circle.")

    def test_integer_value_area(self):
        res = area(25)
        self.assertEqual(res, 625 * pi, "Incorrect on simple radius in area in circle.")

    def test_float_value_area(self):
        res = area(12.5)
        self.assertEqual(res, 156.25 * pi, "Incorrect on float radius in area in circle.")


    def test_zero_value_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0 * 0 * pi, "Incorrect on zero radius in perimeter in circle.")

    def test_integer_value_perimeter(self):
        res = perimeter(25)
        self.assertEqual(res, 2 * pi * 25, "Incorrect on simple radius in perimeter in circle.")

    def test_float_value_perimeter(self):
        res = perimeter(12.5)
        self.assertEqual(res, 2 * pi * 12.5, "Incorrect on float radius in perimeter in circle.")

    def test_string_value_perimeter(self):
        try:
            res = perimeter("abc")
        except Exception as error:
            res = error.__class__
        self.assertEqual(res, TypeError, "Incorrect catch exceptions in perimeter in circle.")



def area(r):
    '''
    Возрващает площадь круга
	
	Параметры:
		r (int): радиус круга
	
	Воращаемое значение
		area (float): площадь искомого круга

	Пример вызова:
        circle_area = area(5)
    Результат:
        circle_area = 78.53981633974483
    '''
    return pi * r * r


def perimeter(r):
    '''
    Возрващает периметр круга (длина окружности)
	
	Параметры:
		r (int): радиус круга
	
	Воращаемое значение
		perimeter (float): периметр искомого круга (длина окружности)

	Пример вызова:
        circle_perimeter = perimeter(5)
    Результат:
        circle_perimeter = 31.41592653589793
    '''
    return 2 * pi * r

