import unittest

class SquareTestCase(unittest.TestCase):

    def test_zero_value_area(self):
        result = area(0)
        self.assertEqual(result, 0)

    def test_integer_value_area(self):
        result = area(5)
        self.assertEqual(result, 25)

    def test_float_value_area(self):
        result = area(2.5)
        self.assertEqual(result, 6.25)

    @unittest.expectedFailure
    def test_string_value_area(self):
        result = area("aaa")
        self.assertEqual(result, TypeError)

    def test_integer_value_perimeter(self):
        result = perimeter(5)
        self.assertEqual(result, 20)

    def test_zero_value_perimeter(self):
        result = perimeter(0)
        self.assertEqual(result, 0)

    def test_float_value_perimeter(self):
        result = perimeter(2.5)
        self.assertEqual(result, 10)

    def test_string_value_perimeter(self):
        result = perimeter("a")
        self.assertEqual(result, TypeError)

def area(a):
    '''
    Возвращает площадь заданого квадрата
	
	Параметры:
	    a (int): длина стороны квадрата

	Возвращаемое значение:
	    area (int): площадь искомого квадрата

    Пример вызова:
        square_area = area(5)
    Результат:
        square_area = 25
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр заданого квадрата
	
	Параметры:
	    a (int): длина стороны квадрата

	Возвращаемое значение:
	    периметр (int): перимитр искомого квадрата

    Пример вызова:
        square_perimeter = perimeter(5)
    Результат:
        square_perimeter = 20
    '''
    return 4 * a
