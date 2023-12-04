import unittest
from math import pi
import circle
import rectangle
import square
import triangle


class CircleTest(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertAlmostEqual(pi * 52 ** 2,
                               circle.area(52),
                               places=5)
        self.assertAlmostEqual(pi * 15.9 ** 2,
                               circle.area(15.9),
                               places=5)

    def test_area_large_value(self):
        self.assertAlmostEqual(pi * 52525252 ** 2,
                               circle.area(52525252),
                               places=5)
        self.assertAlmostEqual(pi * 52525252.52 ** 2,
                               circle.area(52525252.52),
                               places=5)

    def test_area_string_value(self):
        self.assertRaises(TypeError, circle.area, "52")

    def test_area_negative_value(self):
        self.assertRaises(ValueError, circle.area, -52)
        self.assertRaises(ValueError, circle.area, -52.52)

    def test_perimeter_positive_value(self):
        self.assertAlmostEqual(2 * pi * 52,
                               circle.perimeter(52),
                               places=5)
        self.assertAlmostEqual(2 * pi * 15.9,
                               circle.perimeter(15.9),
                               places=5)

    def test_perimeter_large_value(self):
        self.assertAlmostEqual(2 * pi * 52525252,
                               circle.perimeter(52525252),
                               places=5)
        self.assertAlmostEqual(2 * pi * 52525252.52,
                               circle.perimeter(52525252.52),
                               places=5)

    def test_perimeter_string_value(self):
        self.assertRaises(TypeError, circle.perimeter, "52")

    def test_perimetr_negative_value(self):
        self.assertRaises(ValueError, circle.perimeter(-52))
        self.assertRaises(ValueError, circle.perimeter(-52.52))


class RectangleTest(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertAlmostEqual(52 * 152,
                               rectangle.area(52, 152),
                               places=5)
        self.assertAlmostEqual(15.9 * 23.74,
                               rectangle.area(15.9, 23.74),
                               places=5)

    def test_area_large_value(self):
        self.assertAlmostEqual(898989 * 52525252,
                               rectangle.area(898989, 52525252),
                               places=5)
        self.assertAlmostEqual(898989.8989 * 52525252.52,
                               rectangle.area(898989.8989, 52525252.52),
                               places=5)

    def test_area_string_value(self):
        self.assertRaises(TypeError, rectangle.area, 52, "52")
        self.assertRaises(TypeError, rectangle.area, "52", 52)
        self.assertRaises(TypeError, rectangle.area, "52", "52")

    def test_area_negative_value(self):
        self.assertRaises(ValueError, rectangle.area, -52, 52.52)
        self.assertRaises(ValueError, rectangle.area, 52, -52.52)
        self.assertRaises(ValueError, rectangle.area, -52, -52.52)

    def test_perimeter_positive_value(self):
        self.assertAlmostEqual((52 + 152) * 2,
                               rectangle.perimeter(52, 152),
                               places=5)
        self.assertAlmostEqual((15.9 + 23.74) * 2,
                               rectangle.perimeter(15.9, 23.74),
                               places=5)

    def test_perimeter_large_value(self):
        self.assertAlmostEqual((898989 + 52525252) * 2,
                               rectangle.perimeter(898989, 52525252),
                               places=5)
        self.assertAlmostEqual((898989.8989 + 52525252.52) * 2,
                               rectangle.perimeter(898989.8989, 52525252.52),
                               places=5)

    def test_perimeter_string_value(self):
        self.assertRaises(TypeError, rectangle.perimeter, 52, "52")
        self.assertRaises(TypeError, rectangle.perimeter, "52", 52)
        self.assertRaises(TypeError, rectangle.perimeter, "52", "52")

    def test_perimetr_negative_value(self):
        self.assertRaises(ValueError, rectangle.area, -52, 52.52)
        self.assertRaises(ValueError, rectangle.area, 52, -52.52)
        self.assertRaises(ValueError, rectangle.area, -52, -52.52)


class SquareTest(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertAlmostEqual(52 ** 2,
                               square.area(52),
                               places=5)
        self.assertAlmostEqual(15.9 ** 2,
                               square.area(15.9),
                               places=5)

    def test_area_large_value(self):
        self.assertAlmostEqual(52525252 ** 2,
                               square.area(52525252),
                               places=5)
        self.assertAlmostEqual(52525252.52 ** 2,
                               square.area(52525252.52),
                               places=5)

    def test_area_string_value(self):
        self.assertRaises(TypeError, square.area, "52")

    def test_area_negative_value(self):
        self.assertRaises(ValueError, square.area, -52)
        self.assertRaises(ValueError, square.area, -52.52)

    def test_perimeter_positive_value(self):
        self.assertAlmostEqual(4 * 52,
                               square.perimeter(52),
                               places=5)
        self.assertAlmostEqual(4 * 15.9,
                               square.perimeter(15.9),
                               places=5)

    def test_perimeter_large_value(self):
        self.assertAlmostEqual(4 * 52525252,
                               square.perimeter(52525252),
                               places=5)
        self.assertAlmostEqual(4 * 52525252.52,
                               square.perimeter(52525252.52),
                               places=5)

    def test_perimeter_string_value(self):
        self.assertRaises(TypeError, square.perimeter, "52")

    def test_perimetr_negative_value(self):
        self.assertRaises(ValueError, square.perimeter(-52))
        self.assertRaises(ValueError, square.perimeter(-52.52))


class TriangleTest(unittest.TestCase):
    def test_area_positive_value(self):
        self.assertAlmostEqual(52 * 152 / 2,
                               triangle.area(52, 152),
                               places=5)
        self.assertAlmostEqual(15.9 * 23.74 / 2,
                               triangle.area(15.9, 23.74),
                               places=5)

    def test_area_large_value(self):
        self.assertAlmostEqual(898989 * 52525252 / 2,
                               triangle.area(898989, 52525252),
                               places=5)
        self.assertAlmostEqual(898989.8989 * 52525252.52 / 2,
                               triangle.area(898989.8989, 52525252.52),
                               places=5)

    def test_area_string_value(self):
        self.assertRaises(TypeError, triangle.area, 52, "52")
        self.assertRaises(TypeError, triangle.area, "52", 52)
        self.assertRaises(TypeError, triangle.area, "52", "52")

    def test_area_negative_value(self):
        self.assertRaises(ValueError, triangle.area, -52, 52.52)
        self.assertRaises(ValueError, triangle.area, 52, -52.52)
        self.assertRaises(ValueError, triangle.area, -52, -52.52)

    def test_perimeter_positive_value(self):
        self.assertAlmostEqual(52 + 152 + 552,
                               triangle.perimeter(52, 152, 552),
                               places=5)
        self.assertAlmostEqual(15.9 + 23.74 + 31.31,
                               triangle.perimeter(15.9, 23.74, 31.31),
                               places=5)

    def test_perimeter_large_value(self):
        self.assertAlmostEqual(898989 + 52525252 + 91919191,
                               triangle.perimeter(898989, 52525252, 91919191),
                               places=5)
        self.assertAlmostEqual(898989.8989 + 52525252.52 + 91919191.9191,
                               triangle.perimeter(898989.8989, 52525252.52, 91919191.9191),
                               places=5)

    def test_perimeter_string_value(self):
        self.assertRaises(TypeError, triangle.perimeter, 52, "52", 52.52)
        self.assertRaises(TypeError, triangle.perimeter, "52", 52.52, 52)
        self.assertRaises(TypeError, triangle.perimeter, 52, 52, "52.52")
        self.assertRaises(TypeError, triangle.perimeter, "52", "52", 52.52)
        self.assertRaises(TypeError, triangle.perimeter, "52", 52, "52.52")
        self.assertRaises(TypeError, triangle.perimeter, 52, "52.52", "52")
        self.assertRaises(TypeError, triangle.perimeter, "52.52", "52", "52")

    def test_perimetr_negative_value(self):
        self.assertRaises(ValueError, triangle.area, -52, 52.52, 71)
        self.assertRaises(ValueError, triangle.area, 52, -52.52, 71)
        self.assertRaises(ValueError, triangle.area, 52, 52.52, -71)
        self.assertRaises(ValueError, triangle.area, -52, -52.52, 71)
        self.assertRaises(ValueError, triangle.area, -52, 52.52, -71)
        self.assertRaises(ValueError, triangle.area, 52, -52.52, -71)
        self.assertRaises(ValueError, triangle.area, -52, -52.52, -71)



if __name__ == '__main__':
    unittest.main()
