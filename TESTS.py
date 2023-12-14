import unittest
import math
import circle
import rectangle
import square
import triangle

class CIRCLETEST(unittest.TestCase):
    def test_c_area_const(self):
        result = circle.area(5)
        self.assertEqual(result, 78.53981633974483)

    def test_c_perimeter_const(self):
        result2 = circle.perimeter(5)
        self.assertEqual(result2, 31.41592653589793)

class RECTANGLETEST(unittest.TestCase):
    def test_r_area_const(self):
        result = rectangle.area(10, 2)
        self.assertEqual(result, 20)

    def test_r_perimeter_const(self):
        result = rectangle.perimeter(10, 2)
        self.assertEqual(result, 24)


class SQUARETEST(unittest.TestCase):

    def test_s_area(self):
        result = square.area(4)
        self.assertEqual(result, 16)

    def test_s_perimeter(self):
        result = square.area(4)
        self.assertEqual(result, 16)

class TRIANGLETEST(unittest.TestCase):

    def test_t_area(self):
        result = triangle.area(2, 3)
        self.assertEqual(result, 3)

    def test_t_peremiter(self):
        result = triangle.perimeter(10, 10, 10)
        self.assertEqual(result, 30)


if __name__ == '__main__':
    unittest.main()
