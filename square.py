import unittest
def area(a):
    '''
    Takes side of the square and returns its area
    Example:
    Print(area(5)) // 25
    '''
    return a * a


def perimeter(a):
    '''
    Takes side of the square and returns its perimeter
    Example:
    Print(perimeter(5)) // 20
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_error_string(self):
        with self.assertRaises(TypeError):
            res = perimeter("5")