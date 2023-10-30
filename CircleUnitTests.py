import unittest
from circle import area
from circle import perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_int_value_one(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_area_int_value_two(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_area_float_value(self):
        res = area(5.5)
        self.assertEqual(res, 95.03317777109123

                         )

    def test_area_big_value(self):
        res = area(10282828)
        self.assertEqual(res, 332181173966215.4)

    def test_area_zero_value(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_int_value_one(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_perimeter_int_value_two(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_perimeter_float_value(self):
        res = perimeter(4.8)
        self.assertEqual(res, 30.159289474462014)

    def test_perimeter_big_value(self):
        res = perimeter(100000)
        self.assertEqual(res, 628318.5307179586)

    def test_perimeter_zero_value(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
