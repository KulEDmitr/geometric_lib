import unittest


def area(a, h):
    '''
    Принимает на вход a и h - сторона треугольника и высота, опущенная на эту сторону
    из противоположной вершины, соответственно, выводит 1/2 * a * h - площадь треугольника
    '''
    return h*a/2


def perimeter(a, b, c):
    '''Принимает на вход a,b,c - стороны треугольника и выводит a+b+c - периметр треугольника'''
    return a+b+c


class TriangleTestCase(unittest.TestCase):
    def test_area_0(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_area_1(self):
        res = area(5, 5)
        self.assertEqual(res, 12.5)

    def test_area_2(self):
        self.assertEqual(area(-1, 2), -1)

    def test_perimeter_0(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_perimeter_1(self):
        res = perimeter(5, 7, 8)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        self.assertRaises(TypeError, perimeter, 1, 2, '3')

    def test_perimeter_3(self):
        self.assertEqual('123', perimeter('1','2','3'))


