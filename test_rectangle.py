import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # Tests: area
    # Correctness testing
    def test_area_int1(self):
        res = area(5, 10)
        self.assertEqual(res, 50)

    def test_area_int2(self):
        res = area(4035, 2064)
        self.assertEqual(res, 8328240)

    # Error processing
    def test_area_float(self):
        with self.assertRaises(TypeError):
            res = area(2.5, 3.7)

    def test_area_string(self):
        with self.assertRaises(TypeError):
            res = area(2, 'a')

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            res = area(10, -3)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            res = area(10, 0)

    # Tests: perimeter
    # Correctness testing
    def test_perimeter_int1(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)

    def test_perimeter_int2(self):
        res = perimeter(604, 2125)
        self.assertEqual(res, 5458)

    # Error processing
    def test_perimeter_float(self):
        with self.assertRaises(TypeError):
            res = perimeter(5.5, 6.7)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError):
            res = perimeter(15, 'a')

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-234, 21)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError):
            res = perimeter(4, 0)


if __name__ == '__main__':
    unittest.main()
