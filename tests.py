import wolframalpha, unittest
import rectangle, square, triangle, circle


class RectangleTestCase(unittest.TestCase):

    def test_rectangle_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2):
            for b in range(2):
                test_result = rectangle.area(a, b)
                result = next(client.query(f'area of rectangle {a}, {b} = ').results).text
                self.assertEqual(test_result, int(result))
                test_result = rectangle.perimeter(a, b)
                result = next(client.query(f'perimeter of rectangle {a}, {b} = ').results).text
                self.assertEqual(test_result, int(result))

    def test_rectangle_non_valid_input(self):
        result = rectangle.area(10, 'a')
        self.assertEqual(result, 0)
        result = rectangle.perimeter(12, 'e')
        self.assertEqual(result, 0)

    def test_rectangle_float_input(self):
        a = 2.5
        b = 5.5
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        test_result = rectangle.perimeter(a, b)
        result = next(client.query(f'perimeter of rectangle {a}, {b} = ').results).text
        self.assertEqual(test_result, float(result))
        test_result = rectangle.area(a, b)
        result = next(client.query(f'area of rectangle {a}, {b} = ').results).text
        self.assertEqual(test_result, float(result))


class SquareTestCase(unittest.TestCase):

    def test_square_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(30):
            test_result = square.area(a)
            result = next(client.query(f'area of square {a}').results).text
            self.assertEqual(test_result, int(result))
        for a in range(30):
            test_result = square.perimeter(a)
            result = next(client.query(f'perimeter of square {a}').results).text
            self.assertEqual(test_result, int(result))

    def test_square_non_valid_input(self):
        result = square.perimeter('e')
        self.assertEqual(result, 0)
        result = square.area('a')
        self.assertEqual(result, 0)

    def test_square_float_input(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        a = 5.5
        test_result = square.perimeter(a)
        result = next(client.query(f'perimeter of square {a}').results).text
        self.assertEqual(test_result, float(result))
        test_result = square.area(a)
        result = next(client.query(f'area of square {a}').results).text
        self.assertEqual(test_result, float(result))


class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_mul(self):
        result = triangle.area(10, 10)
        self.assertEqual(result, 50)

    def test_triangle_area_zero(self):
        result = triangle.area(10, 0)
        self.assertEqual(result, 0)

    def test_triangle_non_valid_triangle(self):
        result = triangle.area(10, 'y')
        self.assertEqual(result, 0)
        result = triangle.perimeter(10, 1, 'x')
        self.assertEqual(result, 0)

    def test_triangle_perimeter_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    if a + b > c and a + c > b and b + c > a:
                        test_result = triangle.perimeter(a, b, c)
                    else:
                        test_result = 'not a possible triangle'
                    result = next(client.query(f'perimeter of triangle {a} {b} {c}').results).text
                    try:
                        result = int(result)
                    except Exception:
                        result = 'not a possible triangle'
                    self.assertEqual(test_result, result)


class CircleTestCase(unittest.TestCase):

    def test_circle_area_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2, 10):
            test_result = round(circle.area(a))
            result = next(client.query(f'area of circle with radius {a}').results).text
            self.assertEqual(test_result, round(float(result[result.rfind("≈") + 1::])))

    def test_circle_perimeter_wolfram(self):
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        for a in range(2, 10):
            test_result = round(circle.perimeter(a))
            result = next(client.query(f'perimeter of circle with radius {a}').results).text
            self.assertEqual(test_result, round(float(result[result.rfind("≈") + 1::])))

    def test_circle_float_input(self):
        a = 5.5
        app_id = "QHP654-RUKEQ9LT5L"
        client = wolframalpha.Client(app_id)
        test_result = round(circle.perimeter(a))
        result = next(client.query(f'perimeter of circle with radius {a}').results).text
        self.assertEqual(test_result, round(float(result[result.rfind("≈") + 1::])))
        test_result = round(circle.area(a))
        result = next(client.query(f'area of circle with radius {a}').results).text
        self.assertEqual(test_result, round(float(result[result.rfind("≈") + 1::])))

    def test_circle_non_valid_input(self):
        result = circle.area('e')
        self.assertEqual(result, 0)
        result = circle.perimeter('x')
        self.assertEqual(result, 0)
