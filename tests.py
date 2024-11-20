import unittest
import circle
import rectangle
import square
import triangle


class MyTestCase(unittest.TestCase):
    def test_rectangle_area1(self):
        self.assertEqual(rectangle.area(5, 4), 20)

    def test_rectangle_area2(self):
        self.assertEqual(rectangle.area(0, 4), 0)

    def test_rectangle_perimeter1(self):
        self.assertEqual(rectangle.perimeter(5, 4), 18)

    def test_rectangle_perimeter2(self):
        self.assertEqual(rectangle.perimeter(2, 2), 8)

    def test_circle_area1(self):
        self.assertAlmostEquals(circle.area(5), 78.539816339745)

    def test_circle_area2(self):
        self.assertEqual(circle.area(0), 0)

    def test_circle_perimeter1(self):
        self.assertAlmostEquals(circle.perimeter(5), 31.415926535898)

    def test_circle_perimeter2(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_square_area1(self):
        self.assertEqual(square.area(5), 25)

    def test_square_area2(self):
        self.assertEqual(square.area(0), 0)

    def test_square_perimeter1(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_square_perimeter2(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_triangle_area1(self):
        self.assertEqual(triangle.area(5, 4), 10)

    def test_triangle_area2(self):
        self.assertEqual(triangle.area(0, 4), 0)

    def test_triangle_perimeter1(self):
        self.assertEqual(triangle.perimeter(5, 4, 3), 12)

    def test_triangle_perimeter2(self):
        self.assertEqual(triangle.perimeter(0, 3, 0), 3)

    def test_rectangle_error1(self):
        with self.assertRaises(ValueError):
            rectangle.area(-1, 5)

    def test_rectangle_error2(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter(2, "a")
    def test_square_error1(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_square_error2(self):
        with self.assertRaises(TypeError):
            square.area("FFFFF")
    def test_circle_error1(self):
        with self.assertRaises(ValueError):
            circle.area(-1000)

    def test_circle_error2(self):
        with self.assertRaises(TypeError):
            circle.perimeter("-----w-w-w-w-w-wwwlwpeodkpwwffjiojoifjopenisovroroivirewiovjreion")
    def test_triangle_error1(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3333, 5, 1010101)

    def test_triangle_error2(self):
        with self.assertRaises(TypeError):
            triangle.area("jsdheihweuzhopasdlkfgovnodsfbzalkdfvndklherskdgj", 209)


if __name__ == '__main__':
    unittest.main()
