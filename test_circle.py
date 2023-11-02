import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    # Tests: area
    # Correctness testing
    def test_area_int1(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_area_int2(self):
        res = area(13216)
        self.assertAlmostEqual(res, 548718916.9460812)

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
        res = perimeter(16)
        self.assertAlmostEqual(res, 100.53096491487338)

    def test_perimeter_int2(self):
        res = perimeter(1245)
        self.assertEqual(res, 7822.5657074385845)

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