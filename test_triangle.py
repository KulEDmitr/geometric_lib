import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # Correctness testing
    # Tests: area
    def test_area_int1(self):
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_int2(self):
        res = area(56, 20)
        self.assertEqual(res, 560)

    def test_area_float(self):
        res = area(54.1, 312)
        self.assertEqual(res, TypeError)

    def test_area_string(self):
        res = area('a', 7)
        self.assertEqual(res, TypeError)

    def test_area_negative(self):
        res = area(-4, 2)
        self.assertEqual(res, ValueError)

    def test_area_zero(self):
        res = area(0, 43)
        self.assertEqual(res, ValueError)

    # Tests: perimeter
    def test_perimeter_int1(self):
        res = perimeter(7, 4, 5)
        self.assertEqual(res, 16)

    def test_perimeter_int2(self):
        res = perimeter(2115, 4134, 3214)
        self.assertEqual(res, 9463)

    def test_perimeter_float(self):
        res = perimeter(6.7, 32, 31.1)
        self.assertEqual(res, TypeError)

    def test_perimeter_string(self):
        res = perimeter('a', 12, 214)
        self.assertEqual(res, TypeError)

    def test_perimeter_negative(self):
        res = perimeter(-234, 51, 23)
        self.assertEqual(res, ValueError)

    def test_perimeter_zero(self):
        res = perimeter(0, 423, 4321)
        self.assertEqual(res, ValueError)


if __name__ == '__main__':
    unittest.main()
