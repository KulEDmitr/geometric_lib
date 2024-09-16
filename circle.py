import math
import unittest


def area(r):
    '''
    принимает на вход радиус круга r, возвращает площадь круга с заданым радиусом
    Ex: >> area(1)
        >> 3,1415
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    принимает на вход радиус круга r, возвращает длину круга с заданым радиусом
    Ex: >> perimeter(0.5)
        >> 3,1415
    '''
    return 2 * math.pi * r


class CircleTests(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(perimeter(1), math.pi * 2)

    def test_circle_area(self):
        self.assertEqual(area(2), 4 * math.pi)

    def test_if_positive_input(self):
        self.assertEqual(area(-5), "Incorrect input")
        self.assertEqual(perimeter(-5), "Incorrect input")

    def test_if_number(self):
        self.assertEqual(area('a'), "Incorrect input")
        self.assertEqual(perimeter('a'), "Incorrect input")