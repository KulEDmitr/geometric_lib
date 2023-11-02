import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # Correctness testing
    # Tests: area
    def test_area_int1(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_area_int2(self):
        res = area(4035, 2064)
        self.assertEqual(res, 8328240)

    def test_area_float(self):
        res = area(2.5, 3.7)
        self.assertEqual(res, TypeError)

    def test_area_string(self):
        res = area(2, 'a')
        self.assertEqual(res, TypeError)

    def test_area_negative(self):
        res = area(10, -3)
        self.assertEqual(res, ValueError)

    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, ValueError)

    # Tests: perimeter
    def test_perimeter_int1(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)

    def test_perimeter_int2(self):
        res = perimeter(604, 2125)
        self.assertEqual(res, 5458)

    def test_perimeter_float(self):
        res = perimeter(5.5, 6.7)
        self.assertEqual(res, TypeError)

    def test_perimeter_string(self):
        res = perimeter(15, 'a')
        self.assertEqual(res, TypeError)

    def test_perimeter_negative(self):
        res = perimeter(-234, 21)
        self.assertEqual(res, ValueError)

    def test_perimeter_zero(self):
        res = perimeter(4, 0)
        self.assertEqual(res, ValueError)


if __name__ == '__main__':
    unittest.main()
