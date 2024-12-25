import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        test_cases = [
            (5, 10, 50),
            (0, 10, 0),
            (5, -10, 0),
        ]
        for width, height, expected in test_cases:
            result = rect_area(width, height)
            self.assertEqual(
                result, expected,
                f"Test failed: rect_area({width}, {height}) = {result}, expected {expected}"
            )

    def test_perimeter(self):
        test_cases = [
            (5, 10, 30),
            (0, 10, 20),
        ]
        for width, height, expected in test_cases:
            result = rect_perimeter(width, height)
            self.assertEqual(
                result, expected,
                f"Test failed: rect_perimeter({width}, {height}) = {result}, expected {expected}"
            )


class TestSquare(unittest.TestCase):
    def test_area(self):
        test_cases = [
            (5, 25),
            (0, 0),
        ]
        for side, expected in test_cases:
            result = square_area(side)
            self.assertEqual(
                result, expected,
                f"Test failed: square_area({side}) = {result}, expected {expected}"
            )

    def test_perimeter(self):
        test_cases = [
            (5, 20),
            (0, 0),
        ]
        for side, expected in test_cases:
            result = square_perimeter(side)
            self.assertEqual(
                result, expected,
                f"Test failed: square_perimeter({side}) = {result}, expected {expected}"
            )


class TestTriangle(unittest.TestCase):
    def test_area(self):
        test_cases = [
            (3, 4, 6),
            (0, 4, 0),
            (-3, 4, 0),
        ]
        for base, height, expected in test_cases:
            result = triangle_area(base, height)
            self.assertEqual(
                result, expected,
                f"Test failed: triangle_area({base}, {height}) = {result}, expected {expected}"
            )

    def test_perimeter(self):
        test_cases = [
            (3, 4, 12),
            (0, 4, 0),
            (-3, 4, 0),
        ]
        for side1, side2, expected in test_cases:
            result = triangle_perimeter(side1, side2)
            self.assertEqual(
                result, expected,
                f"Test failed: triangle_perimeter({side1}, {side2}) = {result}, expected {expected}"
            )


class TestCircle(unittest.TestCase):
    def test_area(self):
        test_cases = [
            (5, 78.54),
            (0, 0),
            (-5, 0),
        ]
        for radius, expected in test_cases:
            result = circle_area(radius)
            self.assertAlmostEqual(
                result, expected, places=2,
                msg=f"Test failed: circle_area({radius}) = {result}, expected {expected}"
            )

    def test_perimeter(self):
        test_cases = [
            (5, 31.42),
            (0, 0),
            (-5, 0),
        ]
        for radius, expected in test_cases:
            result = circle_perimeter(radius)
            self.assertAlmostEqual(
                result, expected, places=2,
                msg=f"Test failed: circle_perimeter({radius}) = {result}, expected {expected}"
            )


if __name__ == "__main__":
    unittest.main()
