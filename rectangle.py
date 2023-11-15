import unittest
def area(a, b):
    '''
    Takes sides of the rectangle and returns its area
    Example:
    Print(area(5,5)) // 25
    '''
    return a * b

def perimeter(a, b):
    '''
    Takes sides of the rectangle and returns its perimeter
    Example:
    Print(area(5,5)) // 20
    '''
    return 2*a + 2*b

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 50)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5",2)