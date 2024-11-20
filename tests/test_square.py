import unittest
from time import time

import square
from config import MAX_EXECUTION_TIME


class SquareAreaTest(unittest.TestCase):
    test_cases = [
        (1, 1, False),
        (2, 4, False),
        (9, 81, False),
        (0, 0, False),
        (8.63, 74.47690000000001, False),
        (6492593, 42153763863649, False),
        (-3, 0, True),
        (-6583.54, 0, True),
    ]

    def test_area(self):
        for input_a, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_a, expected_output=expected_output,
                              want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        square.area(input_a)
                else:
                    result = square.area(input_a)
                    self.assertEqual(expected_output, result,
                                     f"Square area test failed: expected {expected_output}, got {result}")

    def test_area_performance(self):
        for input_a, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_a, expected_output=expected_output,
                              want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        square.area(input_a)
                else:
                    square.area(input_a)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Square area performance test failed: {execution_time} seconds for "
                                     f"square {input_a}")


class SquarePerimeterTest(unittest.TestCase):
    test_cases = [
        (1, 4, False),
        (2, 8, False),
        (9, 36, False),
        (0, 0, False),
        (8.63, 34.52, False),
        (6492593, 25970372, False),
        (-3, 0, True),
        (-6583.54, 0, True),
    ]

    def test_perimeter(self):
        for input_a, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_a, expected_output=expected_output,
                              want_error=want_error):
                if want_error:
                    with self.assertRaises(ValueError):
                        square.perimeter(input_a)
                else:
                    result = square.perimeter(input_a)
                    self.assertEqual(expected_output, result,
                                     f"Square perimeter test failed: expected {expected_output}, got {result}")

    def test_perimeter_performance(self):
        for input_a, expected_output, want_error in self.test_cases:
            with self.subTest(input_a=input_a, expected_output=expected_output,
                              want_error=want_error):
                start_time = time()

                if want_error:
                    with self.assertRaises(ValueError):
                        square.perimeter(input_a)
                else:
                    square.perimeter(input_a)

                execution_time = time() - start_time

                self.assertLessEqual(execution_time, MAX_EXECUTION_TIME,
                                     f"Square perimeter performance test failed: {execution_time} seconds for "
                                     f"square {input_a}")


if __name__ == "__main__":
    unittest.main()
