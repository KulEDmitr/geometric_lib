import math
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_radius_area(self):
        res = area(0);
        self.assertEqual(res, 0)

    @unittest.expectedFailure
    def test_string_value_area(self):
        res = area("abc")
        self.assertEqual(res, TypeError)

    def test_integer_value_area(self):
        res = area(25)
        self.assertEqual(res, 1963.4954084936207)

    def test_float_value_area(self):
        res = area(12.5)
        self.assertEqual(res, 490.8738521234052)


    def test_zero_value_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_integer_value_perimeter(self):
        res = perimeter(25)
        self.assertEqual(res, 157.07963267948966)

    def test_float_value_perimeter(self):
        res = perimeter(12.5)
        self.assertEqual(res, 78.53981633974483)

    @unittest.expectedFailure
    def test_string_value_perimeter(self):
        res = perimeter("abc")
        self.assertEqual(res, TypeError)



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
    return math.pi * r * r


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
    return 2 * math.pi * r

