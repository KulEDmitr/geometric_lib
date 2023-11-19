import unittest
class TestRectangleMethods(unittest.TestCase):
    def tests_normal_data(self):
        self.assertEqual(area(4, 2), 4)
        self.assertEqual(area(5, 2), 5)
        self.assertEqual(perimeter(1, 2, 2), 5)
        self.assertEqual(perimeter(2, 4, 5), 11)


    def test_zeros(self):
        with self.assertRaises(ValueError):
            area(0, 5)
        with self.assertRaises(ValueError):
            area(5, 0)
        with self.assertRaises(ValueError):
            perimeter(0, 2, 4)
        with self.assertRaises(ValueError):
            perimeter(2, 0, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 2, 0)


    def test_neg_numbers(self):
        with self.assertRaises(ValueError):
            area(-1, 5)
        with self.assertRaises(ValueError):
            area(5, -1)
        with self.assertRaises(ValueError):
            perimeter(-1, 2, 4)
        with self.assertRaises(ValueError):
            perimeter(2, -1, 1)
        with self.assertRaises(ValueError):
            perimeter(1, 2, -1)

    
    def test_triangle_existance(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)
        with self.assertRaises(ValueError):
            perimeter(3, 4, 8)


    def test_wrong_types_area(self):
        with self.assertRaises(TypeError):
            area("ab", 3) 
        with self.assertRaises(TypeError):
            area(2, "33")


    def test_wrong_types_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("ab", 3, 5)
        with self.assertRaises(TypeError):
            perimeter(22, "33", 15)
        with self.assertRaises(TypeError):
            perimeter(22, 33, "15")


def area(a, h):
    '''
    Accepts numbers a and h - side length and
    height drawn to it in the triangle, respectively,
    returns the area of a triangle with the given parameters.
        Example: area(4, 2) -> 4
    '''

    return a * h / 2 


def perimeter(a, b, c):
    '''
    Accepts numbers a, b, c - the lengths of the sides of the triangle,
    returns the perimeter of a triangle with the given parameters.
        Example: perimeter(3, 2, 4) -> 9
    '''

    return a + b + c
