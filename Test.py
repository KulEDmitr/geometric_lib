import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle_lab import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    def test_area_int(self):
        self.assertAlmostEqual(circle_area(2), 12.56637061)  # Тест с целым числом
    def test_area_float(self):
        self.assertAlmostEqual(circle_area(1.5), 7.06858347)  # Тест с дробным числом
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)  # Тест с нулевым радиусом

    def test_perimeter_int(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.84955592)  # Тест с целым числом
    def test_perimeter_float(self):
        self.assertAlmostEqual(circle_perimeter(2.5), 15.70796326)  # Тест с дробным числом
    def test_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)  # Тест с нулевым радиусом


class TestRectangle(unittest.TestCase):
    def test_area_int(self):
        self.assertEqual(rectangle_area(2, 3), 6)  # Тест с целыми числами
    def test_area_float(self):
        self.assertEqual(rectangle_area(1.5, 2.5), 3.75)  # Тест с дробными числами
    def test_area_zero(self):
        self.assertEqual(rectangle_area(0, 5), 0)  # Тест с нулевой стороной

    def test_perimeter_int(self):
        self.assertEqual(rectangle_perimeter(2, 3), 10)  # Тест с целыми числами
    def test_perimeter_float(self):
        self.assertAlmostEqual(rectangle_perimeter(1.5, 2.5), 8)  # Тест с дробными числами
    def test_perimeter_zero(self):
        self.assertEqual(rectangle_perimeter(0, 5), 10)  # Тест с нулевой стороной


class TestSquare(unittest.TestCase):
    def test_area_int(self):
        self.assertEqual(square_area(2), 4)  # Тест с целым числом
    def test_area_float(self):
        self.assertAlmostEqual(square_area(1.5), 2.25)  # Тест с дробным числом
    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)  # Тест с нулевой стороной

    def test_perimeter(self):
        self.assertEqual(square_perimeter(2), 8)  # Тест с целым числом
    def test_perimeter_int(self):
        self.assertEqual(square_perimeter(1.5), 6)  # Тест с дробным числом
    def test_perimeter_float(self):
        self.assertEqual(square_perimeter(0), 0)  # Тест с нулевой стороной


class TestTriangle(unittest.TestCase):
    def test_area_int(self):
        self.assertEqual(triangle_area(3, 4), 6)  # Тест с целыми числами
    def test_area_float(self):
        self.assertAlmostEqual(triangle_area(2.5, 3.5), 4.375)  # Тест с дробными числами
    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 5), 0)  # Тест с нулевой стороной

    def test_perimeter_int(self):
        self.assertEqual(triangle_perimeter(3, 5, 7), 15)  # Тест с целыми числами
    def test_perimeter_float(self):
        self.assertEqual(triangle_perimeter(2.5, 3.5, 1.0), 7)  # Тест с дробными числами
    def test_perimeter_zero(self):
        self.assertEqual(triangle_perimeter(0, 5, 6), 11)  # Тест с нулевой стороной


if __name__ == '__main__':
    unittest.main()