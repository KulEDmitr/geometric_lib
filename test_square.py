import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # Tests: area
    # Correctness testing
    def test_area_int1(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_int2(self):
        res = area(23415)
        self.assertEqual(res, 548262225)

    # Error processing
    def test_area_float(self):
        with self.assertRaises(TypeError):
            res = area(54.1)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            res = area('a')

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-4)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res = area(0)

    # Tests: perimeter
    # Correctness testing
    def test_perimeter_int1(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_perimeter_int2(self):
        res = perimeter(2115)
        self.assertEqual(res, 8460)

    # Error processing
    def test_perimeter_float(self):
        with self.assertRaises(TypeError):
            res = perimeter(6.7)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            res = perimeter('a')

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-234)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res = perimeter(0)


if __name__ == '__main__':
    unittest.main()
