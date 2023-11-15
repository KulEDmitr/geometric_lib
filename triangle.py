import unittest
def area(a, h):
    '''
    Takes base and height the triangle and returns its area
    Example:
    Print(perimeter(10,5)) // 25
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Takes sides the triangle and returns its perimeter
    Example:
    Print(perimeter(5,5,5)) // 15
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_equilateral_triangle_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5",2 ,2)