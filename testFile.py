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
        self.assertEqual(result, 0)

    def test_rectangle_area_random_number1(self):
        result = rectangle.area(50, 100)
        self.assertEqual(result, 5000)

    def test_rectangle_area_random_number2(self):
        result = rectangle.area(12, 51)
        self.assertEqual(result, 612)

    def test_rectangle_area_random_number3(self):
        result = rectangle.area(987654321, 1234567890987654321)
        self.assertEqual(result, 1219326312101813747789971041)

    def test_rectangle_area_float_sided1(self):
        result = rectangle.area(2.5, 4)
        self.assertTrue(diff(result, 10) <= eps)

    def test_rectangle_area_float_sided2(self):
        result = rectangle.area(0.5324, 5.1235)
        self.assertTrue(diff(result, 2.7277514) <= eps)

    def test_rectangle_area_float_sided3(self):
        result = rectangle.area(55.87654, 98.12356)
        self.assertTrue(diff(result, 5482.8050252824) <= eps)

    def test_rectangle_perimeter_random_number1(self):
        result = rectangle.perimeter(5, 5)
        self.assertEqual(result, 20)

    def test_rectangle_perimeter_random_number2(self):
        result = rectangle.perimeter(15, 22)
        self.assertEqual(result, 74)

    def test_rectangle_perimeter_random_number3(self):
        result = rectangle.perimeter(8642098532, 8763734768730348768934)
        self.assertEqual(result, 17527469537477981734932)

    def test_rectangle_perimeter_float_number1(self):
        result = rectangle.perimeter(1.5, 5)
        self.assertEqual(result, 13)

    def test_rectangle_perimeter_float_number2(self):
        result = rectangle.perimeter(0.228, 0.696969)
        self.assertTrue(diff(result, 1.849938) <= eps)

    def test_rectangle_perimeter_float_number3(self):
        result = rectangle.perimeter(56.1259, 100.0001)
        self.assertTrue(diff(result, 312.252) <= eps)


class SquareTestCase(unittest.TestCase):

    def test_square_area_random_number1(self):
        result = square.area(2)
        self.assertEqual(result, 4)

    def test_square_area_random_number2(self):
        result = square.area(123)
        self.assertEqual(result, 15129)

    def test_square_area_random_number3(self):
        result = square.area(89756453)
        self.assertEqual(result, 8056220855141209)

    def test_square_area_equals_rectangle1(self):
        result = square.area(12345)
        self.assertEqual(result, rectangle.area(12345, 12345))

    def test_square_area_equals_rectangle2(self):
        result = square.area(658567445)
        self.assertEqual(result, rectangle.area(658567445, 658567445))

    def test_square_area_float_number1(self):
        result = square.area(1.25)
        self.assertTrue(diff(result, 1.5625) <= eps)

    def test_square_area_float_number2(self):
        result = square.area(12.121212)
        self.assertTrue(diff(result, 146.923780348944) <= eps)

    def test_square_perimeter_random_number1(self):
        result = square.perimeter(15)
        self.assertEqual(result, 60)

    def test_square_perimeter_random_number2(self):
        result = square.perimeter(785643)
        self.assertEqual(result, 3142572)

    def test_square_perimeter_equals_rectangle(self):
        result = square.perimeter(327389374)
        self.assertEqual(result, rectangle.perimeter(327389374, 327389374))

    def test_square_perimeter_float_number1(self):
        result = square.perimeter(5.965)
        self.assertTrue(diff(result, 23.86) <= eps)

    def test_square_perimeter_float_number2(self):
        result = square.perimeter(12.4143)
        self.assertTrue(diff(result, 49.6572) <= eps)


class CircleTestCase(unittest.TestCase):

    def test_circle_area_zero_radius(self):
        result = circle.area(0)
        self.assertEqual(result, 0)

    def test_circle_area_random_number1(self):
        result = circle.area(5)
        self.assertTrue(diff(result, 25 * pi) <= eps)

    def test_circle_area_random_number2(self):
        result = circle.area(12341)
        self.assertTrue(diff(result, 152300281 * pi) <= eps, msg=(str(result) + " != " + str(152300281 * pi)))

    def test_circle_area_float_number1(self):
        result = circle.area(0.5)
        self.assertTrue(diff(result, 0.25 * pi) <= eps)

    def test_circle_area_float_number2(self):
        result = circle.area(pi)
        self.assertTrue(diff(result, pi * pi * pi) <= eps)

    def test_circle_perimeter_random_number1(self):
        result = circle.perimeter(1)
        self.assertTrue(diff(result, 2 * pi) <= eps)

    def test_circle_perimeter_random_number2(self):
        result = circle.perimeter(8731)
        self.assertTrue(diff(result, 17462 * pi) <= eps, msg=(str(result) + " != " + str(17462 * pi)))

    def test_circle_perimeter_float_number1(self):
        result = circle.perimeter(0.21)
        self.assertTrue(diff(result, 0.42 * pi) <= eps)

    def test_circle_perimeter_float_number2(self):
        result = circle.perimeter(25.001)
        self.assertTrue(diff(result, 50.002 * pi) <= eps)

    def test_circle_perimeter_zero_radius(self):
        result = circle.perimeter(0)
        self.assertEqual(result, 0)


class TriangleTestCase(unittest.TestCase):

    def test_triangle_area_random_number1(self):
        result = triangle.area(5, 2)
        self.assertEqual(result, 5)

    def test_triangle_area_random_number2(self):
        result = triangle.area(239, 533)
        self.assertEqual(result, 63693.5)

    def test_triangle_area_zero_height(self):
        result = triangle.area(15.3124, 0)
        self.assertEqual(result, 0)

    def test_triangle_area_float_number1(self):
        result = triangle.area(15.1, 2.77)
        self.assertTrue(diff(result, 20.9135) <= eps)

    def test_triangle_area_float_number2(self):
        result = triangle.area(331.1234, 98.67329)
        self.assertTrue(diff(result, 16336.517636993) <= eps)

    def test_triangle_perimeter_random_number1(self):
        result = triangle.perimeter(4, 2, 3)
        self.assertEqual(result, 9)

    def test_triangle_perimeter_random_number2(self):
        result = triangle.perimeter(2134, 3241, 1205)
        self.assertEqual(result, 6580)

    def test_triangle_perimeter_float_number1(self):
        result = triangle.perimeter(5.4321, 5.23412, 0.5)
        self.assertTrue(diff(result, 11.16622) <= eps)

    def test_triangle_perimeter_float_number2(self):
        result = triangle.perimeter(59.9305, 3.237, 58)
        self.assertTrue(diff(result, 121.1675) <= eps)
