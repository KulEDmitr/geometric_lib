import unittest
import rectangle, square, triangle, circle


class RectangleTestCase(unittest.TestCase):

    def test_rectangle(self):
        test_result = rectangle.area(2, 0)
        self.assertEqual(test_result, 0)
        test_result = rectangle.perimeter(2, 2)
        self.assertEqual(test_result, 4)

    def test_rectangle_non_valid_input(self):
        test_result = rectangle.area(10, 'asfw2')
        self.assertEqual(test_result, 0)
        test_result = rectangle.perimeter(12, 'f2samv')
        self.assertEqual(test_result, 0)

    def test_rectangle_float_input(self):
        test_result = rectangle.perimeter(2.5, 3.9)
        self.assertEqual(test_result, 6.4)
        test_result = rectangle.area(11.1, 2.2)
        self.assertEqual(test_result, 24.42)


class SquareTestCase(unittest.TestCase):

    def test_square(self):
        test_result = square.area(5)
        self.assertEqual(test_result, 25)
        test_result = square.perimeter(5)
        self.assertEqual(test_result, 20)

    def test_square_non_valid_input(self):
        test_result = square.perimeter('fl2ksb3l')
        self.assertEqual(test_result, 0)
        test_result = square.area('nlkqsbf')
        self.assertEqual(test_result, 0)

    def test_square_float_input(self):
        test_result = square.perimeter(10.01)
        self.assertEqual(test_result, 20.02)
        test_result = square.area(11.11)
        self.assertEqual(test_result, 123,4321)


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_mul(self):
        test_result = triangle.area(10, 10)
        self.assertEqual(test_result, 50)

    def test_triangle_area_zero(self):
        test_result = triangle.area(10, 0)
        self.assertEqual(test_result, 0)

    def test_triangle_non_valid_triangle(self):
        test_result = triangle.area(10, 'husicwvb')
        self.assertEqual(test_result, 0)
        test_result = triangle.perimeter(10, 1, 'cwsnjvwjv')
        self.assertEqual(test_result, 0)

    def test_triangle_perimeter(self):
        test_result = triangle.perimeter(213, 421, 421)
        self.assertEqual(1055, test_result)


class CircleTestCase(unittest.TestCase):

    def test_circle_area(self):
        test_result = round(circle.area(10))
        self.assertEqual(test_result, 314)

    def test_circle_perimeter_wolfram(self):
        test_result = round(circle.perimeter(42))
        self.assertEqual(test_result, 264)

    def test_circle_float_input(self):
        test_result = round(circle.perimeter(25.52))
        self.assertEqual(test_result,  160)
        test_result = round(circle.area(42.24))
        self.assertEqual(test_result, 5602)

    def test_circle_non_valid_input(self):
        result = circle.area('feqnouq')
        self.assertEqual(result, 0)
        result = circle.perimeter('cmpswdig')
        self.assertEqual(result, 0)