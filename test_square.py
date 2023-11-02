import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    # Correctness testing
    # Tests: area
    def test_area_int1(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_int2(self):
        res = area(23415)
        self.assertEqual(res, 548262225)

    def test_area_float(self):
        res = area(54.1)
        self.assertEqual(res, TypeError)

    def test_area_string(self):
        res = area('a')
        self.assertEqual(res, TypeError)

    def test_area_negative(self):
        res = area(-4)
        self.assertEqual(res, ValueError)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, ValueError)

    # Tests: perimeter
    def test_perimeter_int1(self):
        res = perimeter(7)
        self.assertEqual(res, 28)

    def test_perimeter_int2(self):
        res = perimeter(2115)
        self.assertEqual(res, 8460)

    def test_perimeter_float(self):
        res = perimeter(6.7)
        self.assertEqual(res, TypeError)

    def test_perimeter_string(self):
        res = perimeter('a')
        self.assertEqual(res, TypeError)

    def test_perimeter_negative(self):
        res = perimeter(-234)
        self.assertEqual(res, ValueError)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, ValueError)


if __name__ == '__main__':
    unittest.main()
