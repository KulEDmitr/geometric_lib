import unittest


def area(a):
    """
    Принимает число а, возвращает произведение a на а;
    Например: area(5) вернет 25
    """
    return a * a


def perimeter(a):
    """
    Принимает число а, возвращает произведение удвоенное a + a;
    Например: perimetr(8) вернет 32
    """
    return 4 * a

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_typical_perim(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

