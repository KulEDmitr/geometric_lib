import unittest

def area(a: float, h: float) -> float:
    """
    Возвращает площадь треугольника с длиной основания a и высотой h

    Параметры:
        a (float): длина основания треугольника
        h (float): высота треугольника

    Возвращаемое значение:
        triangle_area (float): Площадь треугольника с заданными основанием и высотой
    """
    return a * h / 2

def perimeter(a: float, b: float, c: float) -> float:
    """
    Возвращает периметр треугольника с длиной основания a и высотой h

    Параметры:
        a, b, c (float): длины сторон треугольника

    Возвращаемое значение:
        triangle_perimeter (float): Периметр треугольника с заданными сторонами
    """
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 1123)
        self.assertEqual(res, 0)
        res = area(494, 0)
        self.assertEqual(res, 0)
        res = area("0", "129")
        self.assertEqual(res, 0)

    def test_area(self):
        res = area(2, 123)
        self.assertEqual(res, 123)
        res = area(1, 111)
        self.assertEqual(res, 55.5)
        res = area("4", "2")
        self.assertEqual(res, 4)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        res = perimeter(0, "0", "0")
        self.assertEqual(0, res)

    def test_perimeter(self):
        res = perimeter(0, 1034, 32)
        self.assertEqual(res, 1066)
        res = perimeter("1", "2", "3")
        res = perimeter(2, 3, 100)
        self.assertRaises(Exception)