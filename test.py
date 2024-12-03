import unittest
import rectangle
import square
import triangle
import circle

class RectangleAreaTestCase(unittest.TestCase):
    def test_int_test(self):
        res = rectangle.area(2, 3)
        self.assertEqual(res, 6)

    def test_float_test(self):
        res = rectangle.area(4.3738, 2.90432)
        self.assertEqual(round(res, 5), 12.70291)

    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            rectangle.area(10, -10)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.area("a", 10)

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_int_test(self):
        res = rectangle.perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_float_test(self):
        res = rectangle.perimeter(4.3738, 2.90432)
        self.assertEqual(round(res, 5), 14.55624)

    def test_zero_mul(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(10, -10)

    def test_string(self):
        with self.assertRaises(TypeError):
            rectangle.perimeter("a", 10)

class SquareAreaTestCase(unittest.TestCase):
    def test_int_test(self):
        res = square.area(2)
        self.assertEqual(res, 4)

    def test_float_test(self):
        res = square.area(2.90432)
        self.assertEqual(round(res, 5), 8.43507)

    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            square.area(-10)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.area("a")

class SquarePerimeterTestCase(unittest.TestCase):
    def test_int_test(self):
        res = square.perimeter(2)
        self.assertEqual(res, 8)

    def test_float_test(self):
        res = square.perimeter(2.90432)
        self.assertEqual(round(res, 5), 11.61728)

    def test_zero_mul(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            square.perimeter(-10)

    def test_string(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")

class CircleAreaTestCase(unittest.TestCase):
    def test_int_test(self):
        res = circle.area(2)
        self.assertEqual(round(res, 5), 12.56637)

    def test_float_test(self):
        res = circle.area(2.90432)
        self.assertEqual(round(res, 5), 26.49957)

    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            circle.area(-10)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle.area("a")

class CirclePerimeterTestCase(unittest.TestCase):
    def test_int_test(self):
        res = circle.perimeter(2)
        self.assertEqual(round(res, 5), 12.56637)

    def test_float_test(self):
        res = circle.perimeter(2.90432)
        self.assertEqual(round(res, 5), 18.24838)

    def test_zero_mul(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-10)

    def test_string(self):
        with self.assertRaises(TypeError):
            circle.perimeter("a")
        
class TriangleAreaTestCase(unittest.TestCase):
    def test_int_test(self):
        res = triangle.area(2, 3)
        self.assertEqual(res, 3)

    def test_float_test(self):
        res = triangle.area(4.3738, 2.90432)
        self.assertEqual(round(res, 5), 6.35146)

    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            triangle.area(10, -10)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 10)

class TrianglePerimeterTestCase(unittest.TestCase):
    def test_int_test(self):
        res = triangle.perimeter(2, 3, 4)
        self.assertEqual(res, 9)

    def test_float_test(self):
        res = triangle.perimeter(4.3738, 2.90432, 7.79891)
        self.assertEqual(round(res, 5), 15.07703)

    def test_not_existing_tr(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(10, 1, 2)
    
    def test_negative_num(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(10, -10, 8)

    def test_string(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("a", 10, 8)