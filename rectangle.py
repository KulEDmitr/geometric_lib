import unittest

def area(a: float, b: float) -> float:
    """
    Возвращает площадь прямоугольника со сторонами a и b

    Параметры:
    	a, b (float): стороны прямоугольника

    Возвращаемое значение:
    	rectangle_area (float): Площадь прямоугольника с заданными сторонами
    """
    return a * b

def perimeter(a, b):
    """
    Возвращает периметр прямоугольника со сторонами a и b

    Параметры:
        a, b (float): стороны прямоугольника

    Возвращаемое значение:
        rectangle_perimeter (float): Периметр прямоугольника с заданными сторонами
    """

    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area(self):
        res = area(12, 150)
        self.assertEqual(res, 1800)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_square_perimeter(self):
        res = perimeter(7, 7)
        self.assertEqual(res, 28)

    def test_perimeter(self):
        res = perimeter(19, 2)
        self.assertEqual(res, 42)
