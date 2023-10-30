import unittest
from rectangle import area
from rectangle import perimeter


class RectangleTestCase(unittest.TestCase):
    # block of area tests
    def test_area_int_value_one(self):
        res = area(2, 5)
        self.assertEqual(res, 10)

    def test_area_int_value_two(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_big_value(self):
        res = area(3030303, 282828)
        self.assertEqual(res, 857_054_536_884)

    def test_area_float_value(self):
        res = area(2.4, 5.3)
        self.assertEqual(res, float(12.72))

    def test_area_square(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_area_zero_value(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_string_value(self):
        res = area(10, "ab")
        self.assertEqual(res, TypeError)

    def test_area_negative_value(self):
        res = area(-10, 5)
        self.assertEqual(res, TypeError)

    # block for perimeter test
    def test_perimeter_int_value_one(self):
        res = perimeter(10, 2)
        self.assertEqual(res, 24)

    def test_perimeter_int_value_two(self):
        res = perimeter(11, 3)
        self.assertEqual(res, 28)

    def test_perimeter_big_value(self):
        res = perimeter(10000, 282828)
        self.assertEqual(res, 585656)

    def test_perimeter_square(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_perimeter_float_value(self):
        res = perimeter(10.1, 2.3)
        self.assertEqual(res, float(24.8))

    def test_perimeter_zero_value(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_string_value(self):
        res = perimeter(10, "ab")
        self.assertEqual(res, TypeError)

    def test_perimeter_negative_value(self):
        res = perimeter(-10, 5)
        self.assertEqual(res, TypeError)


if __name__ == '__main__':
    unittest.main()
