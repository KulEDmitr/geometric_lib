import unittest


def area(a):
    '''
    принимает на вход сторону квадрата a, возвращает площадь квадрата со стороной a
    Ex: >> area(3)
        >> 9
    '''
    return a * a


def perimeter(a):
    '''
    принимает на вход сторону квадрата a, возвращает периметр квадрата со стороной a
    Ex: >> perimeter(3)
        >> 12
    '''
    return 4 * a


class SquareTests(unittest.TestCase):
    def test_square(self):
        self.assertEqual(perimeter(4), 16)

    def test_square_area(self):
        self.assertEqual(area(4), 16)

    def test_if_positive_input(self):
        self.assertEqual(area(-5), "Incorrect input")
        self.assertEqual(perimeter(-5), "Incorrect input")

    def test_if_number(self):
        self.assertEqual(area('a'), "Incorrect input")
        self.assertEqual(perimeter('a'), "Incorrect input")
