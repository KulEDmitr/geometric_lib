import unittest

def area(a: float) -> float:
    """
    Возвращает площадь квадрата со стороной a

    Параметры:
        a (float): сторона квадрата

    Возвращаемое значение:
        square_area (float): Площадь квадрата с заданной стороной
    """
    return a * a


def perimeter(a: float) -> float:
    """
    Возвращает периметр квадрата со стороной a

    Параметры:
        a (float): сторона квадрата

    Возвращаемое значение:
        square_perimeter (float): Периметр квадрата с заданной стороной
    """
    return 4 * a



class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(13)
        self.assertEqual(res, 169)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter(self):
        res = perimeter(101)
        self.assertEqual(res, 404)
