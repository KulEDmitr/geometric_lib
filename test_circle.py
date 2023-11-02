import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    # Correctness testing
    # Tests: area
    def test_area_int1(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_area_int2(self):
        res = area(13216)
        self.assertAlmostEqual(res, 548718916.9460812)

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
        res = perimeter(16)
        self.assertAlmostEqual(res, 100.53096491487338)

    def test_perimeter_int2(self):
        res = perimeter(1245)
        self.assertEqual(res, 7822.5657074385845)

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