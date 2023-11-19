import unittest
class TestRectangleMethods(unittest.TestCase):
    def tests_normal_data(self):
        self.assertEqual(area(5, 5), 25)
        self.assertEqual(area(6, 2), 12)
        self.assertEqual(perimeter(5, 5), 20)
        self.assertEqual(perimeter(3.5, 4), 15)


    def test_zeros(self):
        with self.assertRaises(ValueError):
            area(0, 10)
        with self.assertRaises(ValueError):
            area(10, 0)
        with self.assertRaises(ValueError):    
            perimeter(10, 0)
        with self.assertRaises(ValueError):
            perimeter(0, 10)


    def test_neg_numbers(self):
        with self.assertRaises(ValueError):
            area(-1, 10)
        with self.assertRaises(ValueError):
            area(13, -1)
        with self.assertRaises(ValueError):
            perimeter(-1, 10)
        with self.assertRaises(ValueError):
            perimeter(13, -1)


    def test_wrong_types(self):
        with self.assertRaises(TypeError):
            area("ab", 3)
        with self.assertRaises(TypeError):
            area(4, "33")
        with self.assertRaises(TypeError):
            perimeter("ab", 3)
        with self.assertRaises(TypeError):
            perimeter(4, "33")


def area(a, b):
    '''
    Accepts numbers a and b - the lengths of sides of the rectangle,
    returns area of a rectangle with sides a and b.
        Example: area(3, 2) -> 6
    '''

    return a * b 


def perimeter(a, b):
    '''
    Accepts numbers a and b - the lengths of sides of the rectangle,
    returns the perimeter of a rectangle with sides a and b.
        Example: perimeter(3, 2) -> 10
    '''

    return (a + b) * 2
