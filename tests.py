import unittest
import math

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def test_area_int(self):
        self.assertEqual(circle.area(10), 100 * math.pi)
        self.assertEqual(circle.area(1), math.pi)
        self.assertEqual(circle.area(8723), 76090729 * math.pi)
        self.assertEqual(circle.area(-5), 25 * math.pi)

    def test_area_double(self):
        self.assertEqual(circle.area(1.746), 3.048516 * math.pi)
        self.assertEqual(circle.area(75.89), 5759.2921 * math.pi)
        self.assertAlmostEqual(circle.area(1 / 3), 0.1111111 * math.pi)

    def test_area_invalid_arg(self):
        with self.assertRaises(TypeError):
            circle.area("abc")

    def test_perimeter_int(self):
        self.assertAlmostEqual(circle.perimeter(20), 125.66370614)
        self.assertAlmostEqual(circle.perimeter(134), 841.94683116)
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_double(self):
        self.assertAlmostEqual(circle.perimeter(9 / 7), 8.0783811)
        self.assertAlmostEqual(circle.perimeter(4.329234), 27.20137946)

    def test_perimeter_invalid_arg(self):
        self.assertEqual(circle.perimeter(1e12100000000000), math.inf)
        with self.assertRaises(TypeError):
            circle.perimeter("string")


class RectangleTestCase(unittest.TestCase):
    def test_area_numeric(self):
        self.assertEqual(rectangle.area(2, 5), 10)
        self.assertEqual(rectangle.area(3, 9), 27)
        self.assertAlmostEqual(rectangle.area(52.187, 32.019), 1670.975553)
        self.assertEqual(rectangle.area(0, 13), 0)

    def test_area_invalid_arg(self):
        with self.assertRaises(TypeError):
            rectangle.area("string_value_1", "string_value_2")
        with self.assertRaises(TypeError):
            rectangle.area(5, "string")
        with self.assertRaises(TypeError):
            rectangle.area(17.4, "string")

    def test_perimeter_numeric(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        self.assertEqual(rectangle.perimeter(5.123, 345.75), 701.746)

    def test_perimeter_invalid_arg(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(1.563, "abc")
        with self.assertRaises(TypeError):
            rectangle.perimeter("string_value_1", "string_value_2")


class SquareTestCase(unittest.TestCase):
    def test_area_numeric(self):
        self.assertEqual(square.area(5), 25)
        self.assertAlmostEqual(square.area(5.32), 28.3024)

    def test_area_invalid_arg(self):
        self.assertEqual(square.area(9e175), math.inf)
        with self.assertRaises(TypeError):
            rectangle.area("string", 5.53)

    def test_perimeter_numeric(self):
        self.assertEqual(square.perimeter(14), 56)
        self.assertEqual(square.perimeter(73.216), 292.864)

    def test_perimeter_invalid_arg(self):
        self.assertEqual(square.perimeter(9e310), math.inf)
        with self.assertRaises(TypeError):
            rectangle.perimeter("string", 43.14)
        with self.assertRaises(TypeError):
            rectangle.perimeter(115, "string")


class TriangleTestCase(unittest.TestCase):
    def test_area_numeric(self):
        self.assertEqual(triangle.area(10, 5), 25)
        self.assertEqual(triangle.area(15, 3), 22.5)
        self.assertAlmostEqual(triangle.area(202.743, 84.2943), 8545.03963245)

    def test_area_invalid_arg(self):
        with self.assertRaises(TypeError):
            triangle.area("string", 10)
        with self.assertRaises(TypeError):
            triangle.area("string_value_1", "string_value_2")

    def test_perimeter_numeric(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
        self.assertEqual(triangle.perimeter(23, 25.174, 35.734), 83.908)
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_invalid_arg(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("string_value_1", 47, "string_value_2")
        with self.assertRaises(TypeError):
            triangle.perimeter("string_value_1", "string_value_2", "string_value_3")


if __name__ == '__main__':
    unittest.main()
