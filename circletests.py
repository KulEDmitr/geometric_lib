import unittest
import circle

class CircleTestCase(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_2(self):
        self.assertAlmostEqual(circle.area(10), 314.1592653589793)

    def test_area_3(self):
        self.assertAlmostEqual(circle.area(67.636), 14371.619275936122)

    def test_perimeter_1(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_2(self):
        self.assertAlmostEqual(circle.perimeter(10), 62.83185307179586)

    def test_perimeter_3(self):
        self.assertAlmostEqual(circle.perimeter(67.636), 424.96952143639845)

    def test_area_not_equal(self):
        self.assertNotEqual(circle.area(10), 40)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(circle.perimeter(10), 30)

    # Негативные тесты
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            circle.area(-5)  # Площадь не может быть отрицательной

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-10)  # Периметр не может быть отрицательным

if __name__ == '__main__':
    unittest.main()
