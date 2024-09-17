import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # Tests: area
    # Correctness testing
    def test_area_int1(self):
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_int2(self):
        res = area(56, 20)
        self.assertEqual(res, 560)

    # Error processing
    def test_area_float(self):
        with self.assertRaises(TypeError):
            res = area(54.1, 312)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            res = area('a', 7)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(-4, 2)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res = area(0, 43)

    # Tests: perimeter
    # Correctness testing
    def test_perimeter_int1(self):
        res = perimeter(7, 4, 5)
        self.assertEqual(res, 16)

    def test_perimeter_int2(self):
        res = perimeter(2115, 4134, 3214)
        self.assertEqual(res, 9463)

    # Error processing
    def test_perimeter_float(self):
        with self.assertRaises(TypeError):
            res = perimeter(6.7, 32, 31.1)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            res = perimeter('a', 12, 214)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-234, 51, 23)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res = perimeter(0, 423, 4321)


if __name__ == '__main__':
    unittest.main()
