import unittest
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(0, 8), 0)
        self.assertEqual(rectangle_area(5, -10), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(2, 3), 12)
        self.assertEqual(rectangle_perimeter(0, 10), 0)
    
    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_area("2", 3)

    def test_perimeter_with_string(self):
        with self.assertRaises(TypeError):
            rectangle_perimeter("2", 3)

    def test_area_with_negative(self):
        self.assertNotEqual(rectangle_area(-2, 3), 0)

    def test_perimeter_with_negative(self):
        self.assertNotEqual(rectangle_perimeter(-2, 3), 0)
        



class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(0), 0)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(10), 40)
        self.assertEqual(square_perimeter(0), 0)
    
    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            square_area("4")

    def test_perimeter_with_string(self):
        with self.assertRaises(TypeError):
            square_perimeter("4")

    def test_area_with_negative(self):
        self.assertNotEqual(square_area(-4), 0)

    def test_perimeter_with_negative(self):
        self.assertNotEqual(square_perimeter(-4), 0)



class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(10, 10), 50)
        self.assertEqual(triangle_area(0, 4), 0)
        self.assertEqual(triangle_area(-3 ,-4), 0)

    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 2), 9)
        self.assertEqual(triangle_perimeter(0, 4), 0)
        self.assertEqual(triangle_perimeter(-3, 4), 0)
    
    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            triangle_area("10", "10")

    def test_perimeter_with_string(self):
        with self.assertRaises(TypeError):
            triangle_perimeter("3", "4")

    def test_area_with_negative(self):
        self.assertNotEqual(triangle_area(-3, 4), 0)

    def test_perimeter_with_negative(self):
        self.assertNotEqual(triangle_perimeter(-3, 4), 0)



class CircleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(-5), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.42, places=2)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(-5), 0)

    def test_area_with_string(self):
        with self.assertRaises(TypeError):
            circle_area("a")

    def test_perimeter_with_string(self):
        with self.assertRaises(TypeError):
            circle_perimeter("5")

    def test_area_with_negative(self):
        self.assertNotEqual(circle_area(-5), 0)

    def test_perimeter_with_negative(self):
        self.assertNotEqual(circle_perimeter(-5), 0)


if __name__ == "__main__":
    unittest.main()