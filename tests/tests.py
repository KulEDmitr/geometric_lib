import circle
import rectangle
import square
import triangle
import unittest
from functools import reduce


class TestCircleMethods(unittest.TestCase):
    def test_area_normal_numbers(self):
        self.assertAlmostEqual(circle.area(5), 78.540, places=3)
        self.assertAlmostEqual(circle.area(10), 314.159, places=3)
        self.assertAlmostEqual(circle.area(0), 0, places=3)
        self.assertAlmostEqual(circle.area(12.2), 467.595, places=3)
        self.assertAlmostEqual(circle.area(53.8), 9093.151, places=3)

    def test_area_negative_numbers(self):
        self.assertRaises(Exception, circle.area, -2)

    def test_area_strings(self):
        self.assertRaises(Exception, circle.area, "12421")
        self.assertRaises(Exception, circle.area, "72")

    def test_area_complex_objects(self):
        self.assertRaises(Exception, circle.area, map)

    def test_perimeter_normal_numbers(self):
        self.assertAlmostEqual(circle.perimeter(2), 12.566, places=3)
        self.assertAlmostEqual(circle.perimeter(2.5), 15.708, places=3)
        self.assertAlmostEqual(circle.perimeter(0), 0, places=3)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, circle.perimeter, -2)

    def test_perimeter_strings(self):
        self.assertRaises(Exception, circle.perimeter, "12421")
        self.assertRaises(Exception, circle.perimeter, "72")

    def test_perimeter_complex_objects(self):
        self.assertRaises(Exception, circle.perimeter, map)


class TestRectangleMethods(unittest.TestCase):
    def test_area_normal_numbers(self):
        self.assertAlmostEqual(rectangle.area(5, 2), 10, places=3)
        self.assertAlmostEqual(rectangle.area(2.5, 2), 5, places=3)

    def test_area_negative_numbers(self):
        self.assertRaises(Exception, rectangle.area, -2, 4)

    def test_area_strings(self):
        self.assertRaises(Exception, rectangle.area, "A", 2)
        self.assertRaises(Exception, rectangle.area, "A", "B")

    def test_area_complex_objects(self):
        self.assertRaises(Exception, rectangle.area, map, 2)

    def test_perimeter_normal_numbers(self):
        self.assertAlmostEqual(rectangle.perimeter(2, 2), 8, places=3)
        self.assertAlmostEqual(rectangle.perimeter(2.5, 2), 9, places=3)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, rectangle.perimeter, -2, 2)

    def test_perimeter_strings(self):
        self.assertRaises(Exception, rectangle.perimeter, "a", 2)
        self.assertRaises(Exception, rectangle.perimeter, "a", "b")

    def test_perimeter_complex_objects(self):
        self.assertRaises(Exception, rectangle.perimeter, map, 2)


class TestSquareMethods(unittest.TestCase):
    def test_area_normal_numbers(self):
        self.assertAlmostEqual(square.area(2), 4, places=3)
        self.assertAlmostEqual(square.area(2.5), 6.25, places=3)

    def test_area_negative_numbers(self):
        self.assertRaises(Exception, square.area, -2)

    def test_area_strings(self):
        self.assertRaises(Exception, square.area, "a")

    def test_area_complex_objects(self):
        self.assertRaises(Exception, square.area, map)

    def test_perimeter_normal_numbers(self):
        self.assertAlmostEqual(square.perimeter(2), 8, places=3)
        self.assertAlmostEqual(square.perimeter(2.5), 10, places=3)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, square.perimeter, -2.5)

    def test_perimeter_strings(self):
        self.assertRaises(Exception, square.perimeter, "a")

    def test_perimeter_complex_objects(self):
        self.assertRaises(Exception, square.perimeter, map)


class TestTriangleMethods(unittest.TestCase):
    def test_area_normal_numbers(self):
        self.assertAlmostEqual(triangle.area(2, 5), 5, places=3)
        self.assertAlmostEqual(triangle.area(2, 5.5), 5.5, places=3)

    def test_area_negative_numbers(self):
        self.assertRaises(Exception, triangle.area, 2, -2)

    def test_area_strings(self):
        self.assertRaises(Exception, triangle.area, 2, "a")
        self.assertRaises(Exception, triangle.area, "a", "a")

    def test_area_complex_objects(self):
        self.assertRaises(Exception, triangle.area, map, int)

    def test_perimeter_normal_numbers(self):
        self.assertAlmostEqual(triangle.perimeter(2, 4, 6), 12, places=3)
        self.assertAlmostEqual(triangle.perimeter(2, 4, 0), 6, places=3)

    def test_perimeter_negative_numbers(self):
        self.assertRaises(Exception, triangle.perimeter, 2, 4, -6)

    def test_perimeter_strings(self):
        self.assertRaises(Exception, triangle.perimeter, "a", "b", "c")
        self.assertRaises(Exception, triangle.perimeter, "a", "b", 2)

    def test_perimeter_complex_objects(self):
        self.assertRaises(Exception, triangle.perimeter, map, int, reduce)


if __name__ == '__main__':
    unittest.main()
