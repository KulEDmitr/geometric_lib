import unittest


def area(a, h):
    '''
    принимает на вход a,h - сторону и высоту, проведенную к данной стороне треугольника, соостветственно, возвращает площадь треугольника со стороной a и высотой h
    Ex: >> area(3,4)
        >> 6
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    принимает на вход a,b,c - стороны произвольнош+го треугольника, возвращает периметр треугольника с заданными сторонами
    Ex: >> perimeter(3,4,5)
        >> 12
    '''
    return a + b + c


class TriangleTests(unittest.TestCase):
    def test_triangle(self):
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)

    def test_triangle_area(self):
        self.assertAlmostEqual(area(3, 4), 6)

    def test_if_negative_input(self):
        self.assertEqual(area(-2, 4), "Incorrect input")
        self.assertEqual(area(2, -4), "Incorrect input")
        self.assertEqual(perimeter(-5, 1, 2), "Incorrect input")
        self.assertEqual(perimeter(2, -4, 1), "Incorrect input")
        self.assertEqual(perimeter(7, 1, -2), "Incorrect input")

    def test_if_number(self):
        self.assertEqual(area('a', 'b'), "Incorrect input")
        self.assertEqual(perimeter('a', 'b', 'z'), "Incorrect input")