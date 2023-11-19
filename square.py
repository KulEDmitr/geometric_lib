import unittest
class TestRectangleMethods(unittest.TestCase):
    def tests_normal_data(self):
        self.assertEqual(area(3), 9)
        self.assertEqual(area(4), 16)
        self.assertEqual(perimeter(3), 12)
        self.assertEqual(perimeter(4), 16)


    def test_zeros(self):
        with self.assertRaises(ValueError):
            area(0)
        with self.assertRaises(ValueError):
            perimeter(0)


    def test_neg_numbers(self):
        with self.assertRaises(ValueError):
            area(-2)
        with self.assertRaises(ValueError):
            perimeter(-5)


    def test_wrong_types(self):
        with self.assertRaises(TypeError):
            area("ab") 
        with self.assertRaises(TypeError):
            area("33")
        with self.assertRaises(TypeError):
            perimeter("ab")
        with self.assertRaises(TypeError):
            perimeter("33")


def area(a):
    '''
    Accepts number a - the length of the side of the square,
    returns the area of a square with side a.
        Example: area(6) -> 36
    '''

    return a * a


def perimeter(a):
    '''
    Accepts number a - the length of the side of the square,
    returns the perimeter of a square with side a.
        Example: perimeter(6) -> 24
    '''

    return 4 * a
