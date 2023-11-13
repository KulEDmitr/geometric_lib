import unittest

def area(a, b):
    '''
    принимает на вход a, b - стороны прямоугольника, возвращает площадь прямоугольника с заданными сторонами
    Ex: >> area(2,3)
        >> 6
    '''
    return a * b


def perimeter(a, b):
    '''
    принимает на вход a, b - стороны прямоугольника, возвращает периметр прямоугольника с заданными сторонами
    Ex: >> perimeter(2,3)
        >> 5
    '''
    return 2 * (a + b)


class RectangleTests(unittest.TestCase):
    def test_rectangle_perimeter(self):
        self.assertEqual(perimeter(4, 5), 18)

    def test_rectangle_area(self):
        self.assertEqual(area(4, 5), 20)

    def test_if_negative_input(self):
        self.assertEqual(area(-5, 1), "Incorrect input")
        self.assertEqual(area(2, -4), "Incorrect input")
        self.assertEqual(perimeter(-5, 1), "Incorrect input")
        self.assertEqual(perimeter(2, -4), "Incorrect input")

    def test_if_number(self):
        self.assertEqual(area('a', 'b'), "Incorrect input")
        self.assertEqual(perimeter('a', 'b'), "Incorrect input")