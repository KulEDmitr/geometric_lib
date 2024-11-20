import unittest
from time import time

import circle
from config import MAX_EXECUTION_TIME


class CircleAreaTest(unittest.TestCase):
    test_cases = [
        (1, 3.141592653589793, False),
        (2, 12.566370614359172, False),
        (9, 254.46900494077323, False),
        (0, 0, False),
        (8.63, 233.9760819021417, False),
        (64926593, 1.3243265954214378e+16, False),
        (-1, 0, True),
        (-6583.54, 0, True),
    ]

    def test_area(self):
        for input_radius, expected_output, want_error in self.test_cases:
            with self.subTest(input_radius=input_radius, expected_output=expected_output, want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        circle.area(input_radius)
                else:
                    result = circle.area(input_radius)
                    self.assertEqual(expected_output, result,
                                     f"Circle area test failed: expected {expected_output}, got {result}")

    def test_area_performance(self):
        for input_radius, expected_output, want_error in self.test_cases:
            with self.subTest(input_radius=input_radius, expected_output=expected_output, want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        circle.area(input_radius)
                else:
                    circle.area(input_radius)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Circle area performance test failed: {execution_time} seconds for "
                                     f"radius={input_radius}")


class CirclePerimeterTest(unittest.TestCase):
    test_cases = [
        (1, 6.283185307179586, False),
        (2, 12.566370614359172, False),
        (9, 56.548667764616276, False),
        (0, 0, False),
        (8.63, 54.22388920095983, False),
        (64926593, 407945815.18282896, False),
        (-1, 0, True),
        (-6583.54, 0, True),
    ]

    def test_perimeter(self):
        for input_radius, expected_output, want_error in self.test_cases:
            with self.subTest(input_radius=input_radius, expected_output=expected_output, want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        circle.perimeter(input_radius)
                else:
                    result = circle.perimeter(input_radius)
                    self.assertEqual(expected_output, result,
                                     f"Circle perimeter test failed: expected {expected_output}, got {result}")

    def test_perimeter_performance(self):
        for input_radius, expected_output, want_error in self.test_cases:
            with self.subTest(input_radius=input_radius, expected_output=expected_output, want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        circle.perimeter(input_radius)
                else:
                    circle.perimeter(input_radius)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Circle perimeter performance test failed: {execution_time} seconds for "
                                     f"radius={input_radius}")


if __name__ == "__main__":
    unittest.main()
