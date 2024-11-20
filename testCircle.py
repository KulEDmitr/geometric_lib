import unittest
import circle


class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(3), 28.274, 3)
        self.assertAlmostEqual(circle.area(2), 12.566, 3)

        self.assertRaises(ValueError, circle.area, -5)

    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(3), 18.850, 3)
        self.assertAlmostEqual(circle.perimeter(2), 12.566, 3)

        self.assertRaises(ValueError, circle.perimeter, -5)


if __name__ == '__main__':
    unittest.main()
