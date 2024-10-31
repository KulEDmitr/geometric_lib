import unittest
from time import time

import triangle
from config import MAX_EXECUTION_TIME


class TriangleAreaTest(unittest.TestCase):
    test_cases = [
        ((1, 1), 0.5, False),
        ((1, 3), 1.5, False),
        ((9, 12), 54, False),
        ((0, 0), 0, False),
        ((0, 1), 0, False),
        ((8.63, 2.004), 8.647260000000001, False),
        ((6492593, 6352642), 20622559490353.0, False),
        ((-3, 5), 0, True),
        ((-6583.54, -3), 0, True),
    ]

    def test_area(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_h=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        triangle.area(*input_data)
                else:
                    result = triangle.area(*input_data)
                    self.assertEqual(expected_output, result,
                                     f"Triangle area test failed: expected {expected_output}, got {result}")

    def test_area_performance(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_h=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        triangle.area(*input_data)
                else:
                    triangle.area(*input_data)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Triangle area performance test failed: {execution_time} seconds for "
                                     f"triangle {input_data}")


class TrianglePerimeterTest(unittest.TestCase):
    test_cases = [
        ((1, 1, 1), 3, False),
        ((1, 3, 2), 6, False),
        ((9, 12, 2), 23, False),
        ((0, 0, 0), 0, False),
        ((0, 1, 0), 1, False),
        ((8.63, 2.004, 3.01), 13.644, False),
        ((6492593, 6352642, 56643), 12901878, False),
        ((-3, 5, 3), 0, True),
        ((-6583.54, -3, -2), 0, True),
    ]

    def test_perimeter(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], input_c=input_data[2],
                              expected_output=expected_output, want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        triangle.perimeter(*input_data)
                else:
                    result = triangle.perimeter(*input_data)
                    self.assertEqual(expected_output, result,
                                     f"Triangle perimeter test failed: expected {expected_output}, got {result}")

    def test_perimeter_performance(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], input_c=input_data[2],
                              expected_output=expected_output, want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        triangle.perimeter(*input_data)
                else:
                    triangle.perimeter(*input_data)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Triangle perimeter performance test failed: {execution_time} seconds for "
                                     f"triangle {input_data}")


if __name__ == "__main__":
    unittest.main()
