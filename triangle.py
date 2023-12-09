import unittest


def area(a, h):
    """Принимает основание a и высоту h треугольника и возвращает площадь 
    такого треугольника
    Параметры: a (int) - основание треугольника
               h (int) - высота треугольника
    Возвращает: area (int) - площадь треугольника с указанными параметрами

    print(area(3, 2))
    ---------------------
    3"""
    if (a <= 0) or (h <= 0):
        raise AssertionError("Values must be over 0")
    else:
        return a * h / 2


def perimeter(a, b, c):
    """Принимает стороны a, b, c треугольника и возвращает периметр такого 
    треугольника
    Параметры: a (int) - первая сторона
               b (int) - вторая сторона
               c (int) - третья сторона
    Возвращает: perimeter (int) - периметр треугольника с указанными сторонами

    print(perimeter(3, 2, 3))
    ---------------------
    8"""
    
    if min(a, b, c) <= 0:
        raise AssertionError("Values must be over 0")
    elif (max(a, b, c) > (a + b + c - max(a, b, c))):
        raise AssertionError("Values must be over 0")
    else:
        return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_right(self):
        res = area(5, 7)
        self.assertEqual(res, 17.5)
        res = area(7, 5)
        self.assertEqual(res, 17.5)
        res = area(10, 6)
        self.assertEqual(res, 30)
        res = area(6, 10)
        self.assertEqual(res, 30)

    def test_perim_right(self):
        res = perimeter(8, 10, 6)
        self.assertEqual(res, 24)
        res = perimeter(47, 61, 54)
        self.assertEqual(res, 162)
        res = perimeter(54, 47, 61)
        self.assertEqual(res, 162)
        res = perimeter(32, 32, 32)
        self.assertEqual(res, 96)

    def test_area_errors(self):
        # with self.assertRaises(AssertionError):
        #     area(1)
        # with self.assertRaises(AssertionError):
        #     area("a", 1)
        # with self.assertRaises(AssertionError):
        #     area("a", "b")
        with self.assertRaises(AssertionError):
            area(0, 5)
        with self.assertRaises(AssertionError):
            area(7, 0)
        with self.assertRaises(AssertionError):
            area(0, 0)
        with self.assertRaises(AssertionError):
            area(-5, 5)
        with self.assertRaises(AssertionError):
            area(5, -7)
        with self.assertRaises(AssertionError):
            area(-5, -7)
        # with self.assertRaises(AssertionError):
        #     area(-5, -7, 8)

    def test_perimeter_errors(self):
        # with self.assertRaises(AssertionError):
        #     perimeter(1, 2)
        # with self.assertRaises(AssertionError):
        #     perimeter("a", 1, 2)
        # with self.assertRaises(AssertionError):
        #     perimeter("a", "b", 2)
        # with self.assertRaises(AssertionError):
        #     perimeter("a", "b", "c")
        with self.assertRaises(AssertionError):
            perimeter(0, 1, 2)
        with self.assertRaises(AssertionError):
            perimeter(0, 0, 2)
        with self.assertRaises(AssertionError):
            perimeter(0, 0, 0)
        with self.assertRaises(AssertionError):
            perimeter(-3, 1, 2)
        with self.assertRaises(AssertionError):
            perimeter(-3, -1, 2)
        with self.assertRaises(AssertionError):
            perimeter(-3, -1, -2)
        with self.assertRaises(AssertionError):
            perimeter(4, 2 ,1)
        with self.assertRaises(AssertionError):
            perimeter(3, 6 ,2)
        with self.assertRaises(AssertionError):
            perimeter(5, 4 ,10)
        # with self.assertRaises(AssertionError):
        #     perimeter(-3, -1, -2, 0)