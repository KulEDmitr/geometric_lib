import unittest
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestGeometryFunctions(unittest.TestCase):

    # Тесты для прямоугольника
    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(5, 3), 15)
        self.assertEqual(rectangle_area(90, 3), 270)
        with self.assertRaises(ValueError):
            rectangle_area(-5, 3)
        with self.assertRaises(ValueError):
            rectangle_area(0, 5)
        with self.assertRaises(ValueError):
            rectangle_area(10, -5)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(5, 3), 16)
        self.assertEqual(rectangle_perimeter(10, 5), 30)
        with self.assertRaises(ValueError):
            rectangle_perimeter(-5, 3)
        with self.assertRaises(ValueError):
            rectangle_perimeter(10, -10)

    # Тесты для квадрата
    def test_square_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(90), 8100)
        with self.assertRaises(ValueError):
            square_area(-4)
        with self.assertRaises(ValueError):
            square_area(0)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)
        self.assertEqual(square_perimeter(10), 40)
        with self.assertRaises(ValueError):
            square_perimeter(-4)
        with self.assertRaises(ValueError):
            square_perimeter(0)

    # Тесты для треугольника
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 4), 10)
        self.assertEqual(triangle_area(10, 8), 40)
        with self.assertRaises(ValueError):
            triangle_area(-5, 4)
        with self.assertRaises(ValueError):
            triangle_area(0, 9)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
        self.assertEqual(triangle_perimeter(2, 3, 4), 9)
        with self.assertRaises(ValueError):
            triangle_perimeter(1, 1, 10)
        with self.assertRaises(ValueError):
            triangle_perimeter(0, 1, 10)

    # Тесты для круга
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138, places=6)
        with self.assertRaises(ValueError):
            circle_area(-3)
        with self.assertRaises(ValueError):
            circle_area(0)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(3), 18.84955592153876, places=6)
        with self.assertRaises(ValueError):
            circle_perimeter(0)
        with self.assertRaises(ValueError):
            circle_perimeter(-3)


if __name__ == '__main__':
    unittest.main()
