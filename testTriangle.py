import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_h(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_zero_both(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_perimeter_zero_a(self):
        res = perimeter(0, 10, 20)
        self.assertEqual(res, 30)

    def test_perimeter_zero_b(self):
        res = perimeter(10, 0, 20)
        self.assertEqual(res, 30)

    def test_perimeter_zero_c(self):
        res = perimeter(10, 20, 0)
        self.assertEqual(res, 30)

    def test_perimeter_zero_all(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_mul(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)


if __name__ == '__main__':
    unittest.main()
