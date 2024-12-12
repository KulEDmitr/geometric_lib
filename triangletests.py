import unittest
import triangle

class TriangleTestCase(unittest.TestCase):

    def test_area_1(self):
        self.assertAlmostEqual(triangle.area(7, 8), 28)

    def test_area_2(self):
        self.assertAlmostEqual(triangle.area(10, 10), 50)

    def test_area_3(self):
        self.assertAlmostEqual(triangle.area(7.5, 3.5), 13.125)

    def test_perimeter_1(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_2(self):
        self.assertEqual(triangle.perimeter(10, 6, 8), 24)

    def test_perimeter_3(self):
        self.assertEqual(triangle.perimeter(34.23, 42.34, 23.43), 100)

    def test_area_not_equal(self):
        self.assertNotAlmostEqual(triangle.area(10, 10), 40)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(triangle.perimeter(10, 6, 8), 30)

    # Негативные тесты
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            triangle.area(-1, 5)  # Площадь не может быть отрицательной

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, -4, -5)  # Периметр не может быть отрицательным

if __name__ == '__main__':
    unittest.main()
