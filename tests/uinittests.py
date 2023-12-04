import unittest
from math import pi
import square
import rectangle
import triangle
import circle


EPSILON = 10 ** (-4)


class SquareAreaTest(unittest.TestCase):
    def test_area_positive_int_value(self):
        self.assertEqual(5 ** 2, square.area(5))
        self.assertEqual(42 ** 2, square.area(42))

    def test_area_real_positive_value(self):
        self.assertAlmostEqual(0.54 ** 2, square.area(0.54))
        self.assertAlmostEqual(200.89 ** 2, square.area(200.89))

    def test_area_negative_value(self):
        self.assertRaises(ValueError, square.area, -1)
        self.assertRaises(ValueError, square.area, -30.30)


class SquarePerimeterTest(unittest.TestCase):
    def test_perimeter_positive_int_value(self):
        self.assertEqual(5 * 4, square.perimeter(5))
        self.assertEqual(42 * 4, square.perimeter(42))

    def test_perimeter_real_positive_value(self):
        self.assertAlmostEqual(0.54 * 4, square.perimeter(0.54))
        self.assertAlmostEqual(200.89 * 4, square.perimeter(200.89))

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, square.perimeter, -1)
        self.assertRaises(ValueError, square.perimeter, -30.30)


class RectangleAreaTest(unittest.TestCase):
    def test_positive_int_value(self):
        self.assertEqual(10 * 15, rectangle.area(10, 15))
        self.assertEqual(42 * 1042, rectangle.area(42, 1042))

    def test_area_real_positive_value(self):
        self.assertAlmostEqual(0.54 * 0.47, rectangle.area(0.54, 0.47))
        self.assertAlmostEqual(200.89 * 157.73, rectangle.area(200.89, 157.73))

    def test_area_negative_value(self):
        self.assertRaises(ValueError, rectangle.area, -1, 10)
        self.assertRaises(ValueError, rectangle.area, 15.10, -30.30)


class RectanglePerimeterTest(unittest.TestCase):
    def test_perimeter_positive_int_value(self):
        self.assertEqual((10 + 15) * 2, rectangle.perimeter(10, 15))
        self.assertEqual((42 + 1042) * 2, rectangle.perimeter(42, 1042))

    def test_perimeter_real_positive_value(self):
        self.assertAlmostEqual((0.54 + 0.47) * 2, rectangle.perimeter(0.54, 0.47))
        self.assertAlmostEqual((200.89 + 157.73) * 2, rectangle.perimeter(200.89, 157.73))

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, rectangle.perimeter, -1, 10)
        self.assertRaises(ValueError, rectangle.perimeter, 15.10, -30.30)


class TriangleAreaTest(unittest.TestCase):
    def test_area_positive_int_value(self):
        self.assertEqual(10 * 15 / 2, triangle.area(10, 15))
        self.assertEqual(42 * 1042 / 2, triangle.area(42, 1042))

    def test_area_real_positive_value(self):
        self.assertAlmostEqual(0.54 * 0.47 / 2, triangle.area(0.54, 0.47))
        self.assertAlmostEqual(200.89 * 157.73 / 2, triangle.area(200.89, 157.73))

    def test_area_negative_value(self):
        self.assertRaises(ValueError, triangle.area, -1, 10)
        self.assertRaises(ValueError, triangle.area, 15.10, -30.30)


class TrianglePerimeterTest(unittest.TestCase):
    def test_perimeter_positive_int_value(self):
        self.assertEqual(10 + 10 + 10, triangle.perimeter(10, 10, 10))
        self.assertEqual(100 + 200 + 250, triangle.perimeter(100, 200, 250))

    def test_perimeter_real_positive_value(self):
        self.assertAlmostEqual(0.54 + 0.47 + 0.29, triangle.perimeter(0.54, 0.47, 0.29))
        self.assertAlmostEqual(200.89 + 157.73 + 60.75, triangle.perimeter(200.89, 157.73, 60.75))

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, triangle.perimeter, -1, 10)
        self.assertRaises(ValueError, triangle.perimeter, 15.10, -30.30)

    def test_perimeter_triangle_inequality_value(self):
        self.assertRaises(ValueError, triangle.perimeter, 10, 20, 50)
        self.assertRaises(ValueError, triangle.perimeter, 50, 10, 20)
        self.assertRaises(ValueError, triangle.perimeter, 20, 50, 10)


class CircleAreaTest(unittest.TestCase):
    def test_area_positive_int_value(self):
        self.assertAlmostEqual(pi * 5 ** 2, circle.area(5))
        self.assertAlmostEqual(pi * 42 ** 2, circle.area(42))

    def test_area_real_positive_value(self):
        self.assertAlmostEqual(pi * 0.54 ** 2, circle.area(0.54))
        self.assertAlmostEqual(pi * 200.89 ** 2, circle.area(200.89))

    def test_area_negative_value(self):
        self.assertRaises(ValueError, circle.area, -1)
        self.assertRaises(ValueError, circle.area, -30.30)


class CirclePerimeterTest(unittest.TestCase):
    def test_perimeter_positive_int_value(self):
        self.assertEqual(2 * pi * 5, circle.perimeter(5))
        self.assertEqual(2 * pi * 42, circle.perimeter(42))

    def test_perimeter_real_positive_value(self):
        self.assertAlmostEqual(2 * pi * 0.54, circle.perimeter(0.54))
        self.assertAlmostEqual(2 * pi * 200.89, circle.perimeter(200.89))

    def test_perimeter_negative_value(self):
        self.assertRaises(ValueError, circle.perimeter, -1)
        self.assertRaises(ValueError, circle.perimeter, -30.30)


if __name__ == '__main__':
    unittest.main()
