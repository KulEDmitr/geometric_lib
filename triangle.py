import unittest


def area(a, h):
    '''
    Вычисляет площадь треугольника.

    Args:
        a (float): Длина основания треугольника.
        h (float): Длина высоты, опущенной к основанию.

    Returns:
        float: Площадь треугольника.

    Пример использования:
    import triangle
    base = 6
    height = 4
    area_result = triangle.area(base, height)
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Вычисляет периметр треугольника.

    Args:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.

    Returns:
        float: Периметр треугольника.

    Пример использования:
    import triangle
    side1 = 3
    side2 = 4
    side3 = 5
    perimeter_result = triangle.perimeter(side1, side2, side3)
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_positive_int_values(self):
        res = area(3, 3)
        self.assertAlmostEqual(4.5, res, places=6, msg="Failed for int values")

    def test_area_positive_float_values(self):
        res = area(3.5, 2.5)
        self.assertAlmostEqual(4.375, res, places=6, msg="Failed for float values")

    def test_area_zero_values(self):
        res = area(0, 7)
        self.assertEqual(0, res, "Failed for zero values")

    def test_area_negative_float_values(self):
        with self.assertRaises(ValueError):
            area(-4.8, 7.1)

    def test_area_string_and_string_values(self):
        with self.assertRaises(TypeError):
            area("4", "7")

    def test_area_string_and_int_values(self):
        with self.assertRaises(TypeError):
            area("4", 7)

    def test_area_string_and_float_values(self):
        with self.assertRaises(TypeError):
            area("4", 7.3)

    def test_perimeter_positive_int_values(self):
        res = perimeter(3, 2, 4)
        self.assertEqual(9, res, msg="Failed for int values")

    def test_perimeter_positive_float_values(self):
        res = perimeter(3.5, 2.5, 4.0)
        self.assertAlmostEqual(10.0, res, places=6, msg="Failed for float values")

    def test_perimeter_zero_values(self):
        res = perimeter(0, 5, 0)
        self.assertEqual(res, 5, "Failed for zero values")

    def test_perimeter_negative_float_values(self):
        with self.assertRaises(ValueError):
            perimeter(-3.5, 2.5, -1.0)

    def test_perimeter_string_and_string_values(self):
        with self.assertRaises(TypeError):
            perimeter("3", "5", "4")

    def test_perimeter_string_and_int_values(self):
        with self.assertRaises(TypeError):
            perimeter("3", 5, "4")

    def test_perimeter_string_and_float_values(self):
        with self.assertRaises(TypeError):
            perimeter("3", 5.3, "4.2")
