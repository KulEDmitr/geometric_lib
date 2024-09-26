import unittest
from math import pi
from geometry import rectangle
from geometry import square
from geometry import circle
from geometry import triangle


eps = 0.000000001

def diff(a, b):
    '''
    Функция принимает 2 числа a, b и возвращает разницу между ними
    Input:
        (int/float) a
        (int.float) b
    Output:
        (int/float) abs(a - b)
    Пример:
        print(diff(5, 2.5))
    Output:
        2.5
    '''
    return abs(a - b)


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_area_zero_sided(self):
        result = rectangle.area(1357908642, 0)
        expected = 0
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_random_number1(self):
        result = rectangle.area(50, 100)
        expected = 5000
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_random_number2(self):
        result = rectangle.area(12, 51)
        expected = 612
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_random_number3(self):
        result = rectangle.area(987654321, 1234567890987654321)
        expected = 1219326312101813747789971041
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_float_sided1(self):
        result = rectangle.area(2.5, 4)
        expected = 10
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_float_sided2(self):
        result = rectangle.area(0.5324, 5.1235)
        expected = 2.7277514
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_area_float_sided3(self):
        result = rectangle.area(55.87654, 98.12356)
        expected = 5482.8050252824
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_random_number1(self):
        result = rectangle.perimeter(5, 5)
        expected = 20
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_random_number2(self):
        result = rectangle.perimeter(15, 22)
        expected = 74
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_random_number3(self):
        result = rectangle.perimeter(8642098532, 8763734768730348768934)
        expected = 17527469537477981734932
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_float_number1(self):
        result = rectangle.perimeter(1.5, 5)
        expected = 13
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_float_number2(self):
        result = rectangle.perimeter(0.228, 0.696969)
        expected = 1.849938
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_rectangle_perimeter_float_number3(self):
        result = rectangle.perimeter(56.1259, 100.0001)
        expected = 312.252
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))


class SquareTestCase(unittest.TestCase):

    def test_square_area_random_number1(self):
        result = square.area(2)
        expected = 4
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_area_random_number2(self):
        result = square.area(123)
        expected = 15129
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_area_random_number3(self):
        result = square.area(89756453)
        expected = 8056220855141209
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_area_equals_rectangle1(self):
        result = square.area(12345)
        expected = rectangle.area(12345, 12345)
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_area_equals_rectangle2(self):
        result = square.area(658567445)
        expected = rectangle.area(658567445, 658567445)
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_area_float_number1(self):
        result = square.area(1.25)
        expected = 1.5625
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_square_area_float_number2(self):
        result = square.area(12.121212)
        expected = 146.923780348944
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_square_perimeter_random_number1(self):
        result = square.perimeter(15)
        expected = 60
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_perimeter_random_number2(self):
        result = square.perimeter(785643)
        expected = 3142572
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_perimeter_equals_rectangle(self):
        result = square.perimeter(327389374)
        expected = rectangle.perimeter(327389374, 327389374)
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_square_perimeter_float_number1(self):
        result = square.perimeter(5.965)
        expected = 23.86
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_square_perimeter_float_number2(self):
        result = square.perimeter(12.4143)
        expected = 49.6572
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))


class CircleTestCase(unittest.TestCase):

    def test_circle_area_zero_radius(self):
        result = circle.area(0)
        expected = 0
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_circle_area_random_number1(self):
        result = circle.area(5)
        expected = 25 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_area_random_number2(self):
        result = circle.area(12341)
        expected = 152300281 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_area_float_number1(self):
        result = circle.area(0.5)
        expected = 0.25 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_area_float_number2(self):
        result = circle.area(pi)
        expected = pi * pi * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_perimeter_random_number1(self):
        result = circle.perimeter(1)
        expected = 2 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_perimeter_random_number2(self):
        result = circle.perimeter(8731)
        expected = 17462 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_perimeter_float_number1(self):
        result = circle.perimeter(0.21)
        expected = 0.42 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_perimeter_float_number2(self):
        result = circle.perimeter(25.001)
        expected = 50.002 * pi
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_circle_perimeter_zero_radius(self):
        result = circle.perimeter(0)
        expected = 0
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area_random_number1(self):
        result = triangle.area(5, 2)
        expected = 5
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_triangle_area_random_number2(self):
        result = triangle.area(239, 533)
        expected = 63693.5
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_triangle_area_zero_height(self):
        result = triangle.area(15.3124, 0)
        expected = 0
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_triangle_area_float_number1(self):
        result = triangle.area(15.1, 2.77)
        expected = 20.9135
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_triangle_area_float_number2(self):
        result = triangle.area(331.1234, 98.67329)
        expected = 16336.517636993
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_triangle_perimeter_random_number1(self):
        result = triangle.perimeter(4, 2, 3)
        expected = 9
        self.assertEqual(result, expected)

    def test_triangle_perimeter_random_number2(self):
        result = triangle.perimeter(2134, 3241, 1205)
        expected = 6580
        self.assertEqual(result, expected, msg=(str(result) + " != " + str(expected)))

    def test_triangle_perimeter_float_number1(self):
        result = triangle.perimeter(5.4321, 5.23412, 0.5)
        expected = 11.16622
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))

    def test_triangle_perimeter_float_number2(self):
        result = triangle.perimeter(59.9305, 3.237, 58)
        expected = 121.1675
        self.assertTrue(diff(result, expected) <= eps, msg=(str(result) + " != " + str(expected)))
