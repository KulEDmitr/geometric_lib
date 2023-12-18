import math


def area(r):
    '''принимает радиус - возвращает площадь круга
    r = 3
    area = 28.274333882308138
    '''
    return math.pi * r * r


def perimeter(r):
    '''принимает радиус - возвращает периметр круга
    r = 3
    perimeter = 18.84955592153876
    '''
    return 2 * math.pi * r


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_negative_value(self):
        res = area(-10)
        self.assertEqual(res, 314.1592653589793)
