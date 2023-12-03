import unittest
import math

import rectangle
import circle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    '''
    Unit tests for rectangle.py

        Check:
            function: rectangle.area(a, b)
            function: rectangle.perimeter(a, b)

        Return:
            OK, if check is successfully
            FAILED, if check isn't successfully
    '''
    # tests for area
    def test_ordinary_case_area(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)

    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_letter_area(self):
        self.assertRaises(TypeError, rectangle.area, 'a', 5)

    def test_letter_negative_area(self):
        self.assertRaises(TypeError, rectangle.area, 'a', -3)

    def test_one_negative_area(self):
        self.assertRaises(TypeError, rectangle.area, -3, 1)

    def test_two_negative_area(self):
        self.assertRaises(TypeError, rectangle.area, -10, -3)

    # test for perimeter
    def test_ordinary_case_perimeter(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_letter_perimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, 'a', 2)

    def test_letter_negative_perimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, 'a', -3)

    def test_negative_perimeter(self):
        self.assertRaises(TypeError, rectangle.perimeter, -3, -3)


class SquareTestCase(unittest.TestCase):
    '''
    Unit tests for square.py

        Check:
            function: square.area(a)
            function: square.perimeter(a)

        Return:
            OK, if check is successfully
            FAILED, if check isn't successfully
    '''
    # tests for area
    def test_ordinary_case_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_letter_area(self):
        self.assertRaises(TypeError, square.area, 'a')

    def test_negative_area(self):
        self.assertRaises(TypeError, square.area, -5)

    # test for perimeter
    def test_ordinary_case_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_letter_perimeter(self):
        self.assertRaises(TypeError, square.perimeter, 'a')

    def test_negative_perimeter(self):
        self.assertRaises(TypeError, square.perimeter, -5)


class CircleTestCase(unittest.TestCase):
    '''
    Unit tests for circle.py

        Check:
            function: circle.area(r)
            function: circle.perimeter(r)

        Return:
            OK, if check is successfully
            FAILED, if check isn't successfully
    '''
    # tests for area
    def test_ordinary_case_area(self):
        res = circle.area(2)
        self.assertAlmostEqual(res, 4 * math.pi, places=7)

    def test_zero_area(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_letter_area(self):
        self.assertRaises(TypeError, circle.area, 'a')

    def test_negative_area(self):
        self.assertRaises(TypeError, circle.area, -2)

    # test for perimeter
    def test_ordinary_case_perimeter(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, 6 * math.pi, places=7)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_letter_perimeter(self):
        self.assertRaises(TypeError, circle.perimeter, 'a')

    def test_negative_perimeter(self):
        self.assertRaises(TypeError, circle.perimeter, -3)


class TriangleTestCase(unittest.TestCase):
    '''
    Unit tests for triangle.py

        Check:
            function: triangle.area(a, h)
            function: triangle.perimeter(a, b, c)

        Return:
            OK, if check is successfully
            FAILED, if check isn't successfully
    '''
    # tests for area
    def test_ordinary_case_area(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_zero_area(self):
        res = triangle.area(3, 0)
        self.assertEqual(res, 0)

    def test_letter_area(self):
        self.assertRaises(TypeError, triangle.area, 'a', 3)

    def test_letter_negative_area(self):
        self.assertRaises(TypeError, triangle.area, 'a', -3)

    def test_one_negative_area(self):
        self.assertRaises(TypeError, triangle.area, 3, -4)

    def test_two_negative_area(self):
        self.assertRaises(TypeError, triangle.area, -3, -4)

    # test for perimeter
    def test_ordinary_case_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimeter(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_letter_perimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, 'a', 4, 5)

    def test_letter_negative_perimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, 'a', -4, -5)

    def test_negative_perimeter(self):
        self.assertRaises(TypeError, triangle.perimeter, -3, -4, -5)