import unittest
import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(0, res)
        res = rectangle.area(0, 10)
        self.assertEqual(0, res)
        res = rectangle.area(0, 0)
        self.assertEqual(0, res)

    def test_normal_mul(self):
        res = rectangle.area(10, 7)
        self.assertEqual(70, res)
        res = rectangle.area(7, 10)
        self.assertEqual(70, res)

    def test_string_mul(self):
        with self.assertRaises(TypeError):
            rectangle.area('a', 'b')
        with self.assertRaises(TypeError):
            rectangle.area(2, 'b')
        with self.assertRaises(TypeError):
            rectangle.area('a', 3)

    def test_negative_mul(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, -5)
        with self.assertRaises(ValueError):
            rectangle.area(2, -5)
        with self.assertRaises(ValueError):
            rectangle.area(-5, 3)

    # perimetr tests
    def test_zero_per(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(0, res)
        res = rectangle.perimeter(0, 10)
        self.assertEqual(0, res)
        res = rectangle.perimeter(0, 0)
        self.assertEqual(0, res)

    def test_normal_per(self):
        res = rectangle.perimeter(10, 7)
        self.assertEqual(34, res)
        res = rectangle.perimeter(7, 10)
        self.assertEqual(34, res)

    def test_string_per(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter('a', 'b')
        with self.assertRaises(TypeError):
            rectangle.perimeter(2, 'b')
        with self.assertRaises(TypeError):
            rectangle.perimeter('a', 3)

    def test_negative_per(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, -5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(2, -5)
        with self.assertRaises(ValueError):
            rectangle.perimeter(-5, 3)


class SquareTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(0, res)

    def test_normal_mul(self):
        res = square.area(10)
        self.assertEqual(100, res)

    def test_string_mul(self):
        with self.assertRaises(TypeError):
            square.area('a')

    def test_negative_mul(self):
        with self.assertRaises(ValueError):
            square.area(-5)

    # perimetr tests
    def test_zero_per(self):
        res = square.perimeter(0)
        self.assertEqual(0, res)

    def test_normal_per(self):
        res = square.perimeter(10)
        self.assertEqual(40, res)

    def test_string_per(self):
        with self.assertRaises(TypeError):
            square.perimeter('a')

    def test_negative_per(self):
        with self.assertRaises(ValueError):
            square.perimeter(-5)


class CircleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(0, res)

    def test_normal_mul(self):
        res = circle.area(16)
        self.assertEqual(804.247719318987, res)

    def test_string_mul(self):
        with self.assertRaises(TypeError):
            circle.area('a')

    def test_negative_mul(self):
        with self.assertRaises(ValueError):
            circle.area(-5)

    # perimetr tests
    def test_zero_per(self):
        res = circle.perimeter(0)
        self.assertEqual(0, res)

    def test_normal_per(self):
        res = circle.perimeter(25)
        self.assertEqual(157.07963267948966, res)

    def test_string_per(self):
        with self.assertRaises(TypeError):
            circle.perimeter('a')

    def test_negative_per(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-5)


class TriangleTestCase(unittest.TestCase):
    # area tests
    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(0, res)
        res = triangle.area(0, 10)
        self.assertEqual(0, res)
        res = triangle.area(0, 0)
        self.assertEqual(0, res)

    def test_normal_mul(self):
        res = triangle.area(16, 5)
        self.assertEqual(40, res)
        res = triangle.area(5, 16)
        self.assertEqual(40, res)

    def test_string_mul(self):
        with self.assertRaises(TypeError):
            triangle.area('a', 'b')
        with self.assertRaises(TypeError):
            triangle.area(2, 'b')
        with self.assertRaises(TypeError):
            triangle.area('a', 3)

    def test_negative_mul(self):
        with self.assertRaises(ValueError):
            triangle.area(-5, -5)
        with self.assertRaises(ValueError):
            triangle.area(2, -5)
        with self.assertRaises(ValueError):
            triangle.area(-5, 3)

    # perimetr tests
    def test_zero_per(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(0, res)
        res = triangle.perimeter(0, 0, 1)
        self.assertEqual(0, res)
        res = triangle.perimeter(0, 1, 0)
        self.assertEqual(0, res)
        res = triangle.perimeter(0, 1, 1)
        self.assertEqual(0, res)
        res = triangle.perimeter(1, 0, 0)
        self.assertEqual(0, res)
        res = triangle.perimeter(1, 0, 1)
        self.assertEqual(0, res)
        res = triangle.perimeter(1, 1, 0)
        self.assertEqual(0, res)
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(0, res)

    def test_normal_per(self):
        res = triangle.perimeter(25, 30, 10)
        self.assertEqual(65, res)
        res = triangle.perimeter(25, 10, 30)
        self.assertEqual(65, res)
        res = triangle.perimeter(30, 25, 10)
        self.assertEqual(65, res)
        res = triangle.perimeter(30, 10, 25)
        self.assertEqual(65, res)
        res = triangle.perimeter(10, 30, 25)
        self.assertEqual(65, res)
        res = triangle.perimeter(10, 25, 30)
        self.assertEqual(65, res)

    def test_string_per(self):
        with self.assertRaises(TypeError):
            triangle.perimeter('a', 'b', 'c')
        with self.assertRaises(TypeError):
            triangle.perimeter('a', 'b', 1)
        with self.assertRaises(TypeError):
            triangle.perimeter('a', 1, 'c')
        with self.assertRaises(TypeError):
            triangle.perimeter('a', 1, 1)
        with self.assertRaises(TypeError):
            triangle.perimeter(1, 'b', 'c')
        with self.assertRaises(TypeError):
            triangle.perimeter(1, 'b', 1)
        with self.assertRaises(TypeError):
            triangle.perimeter(1, 1, 'c')

    def test_negative_per(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, -5, -5)
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, -5, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 1, -5)
        with self.assertRaises(ValueError):
            triangle.perimeter(-5, 1, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, -5, -5)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, -5, 1)
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, -5)


if __name__ == '__main__':
    unittest.main()
