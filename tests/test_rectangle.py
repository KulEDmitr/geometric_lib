import unittest
from time import time

import rectangle
from config import MAX_EXECUTION_TIME


class RectangleAreaTest(unittest.TestCase):
    test_cases = [
        ((1, 1), 1, False),
        ((1, 2), 2, False),
        ((9, 12), 108, False),
        ((0, 0), 0, False),
        ((0, 1), 0, False),
        ((8.63, 2.004), 17.294520000000002, False),
        ((6492593, 6352642), 41245118980706, False),
        ((-3, 5), 0, True),
        ((-6583.54, -3), 0, True),
    ]

    def test_area(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        rectangle.area(*input_data)
                else:
                    result = rectangle.area(*input_data)
                    self.assertEqual(expected_output, result,
                                     f"Rectangle area test failed: expected {expected_output}, got {result}")

    def test_area_performance(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        rectangle.area(*input_data)
                else:
                    rectangle.area(*input_data)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Rectangle area performance test failed: {execution_time} seconds for "
                                     f"rectangle {input_data}")


class RectanglePerimeterTest(unittest.TestCase):
    test_cases = [
        ((1, 1), 4, False),
        ((1, 2), 6, False),
        ((9, 12), 42, False),
        ((0, 0), 0, False),
        ((0, 1), 2, False),
        ((8.63, 2.004), 21.268, False),
        ((6492593, 6352642), 25690470, False),
        ((-3, 5), 0, True),
        ((-6583.54, -3), 0, True),
    ]

    def test_perimeter(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        rectangle.perimeter(*input_data)
                else:
                    result = rectangle.perimeter(*input_data)
                    self.assertEqual(expected_output, result,
                                     f"Rectangle perimeter test failed: expected {expected_output}, got {result}")

    def test_perimeter_performance(self):
        for input_data, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_data[0], input_b=input_data[1], expected_output=expected_output,
                              want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        rectangle.perimeter(*input_data)
                else:
                    rectangle.perimeter(*input_data)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Rectangle perimeter performance test failed: {execution_time} seconds for "
                                     f"rectangle {input_data}")


if __name__ == "__main__":
    unittest.main()
