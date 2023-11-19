import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 
