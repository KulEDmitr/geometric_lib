import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(rectangle.area(0, 13), 0)

    def test_area_2(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_3(self):
        self.assertAlmostEqual(rectangle.area(65.5, 4.5), 294.75)

    def test_perimeter_1(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_2(self):
        self.assertEqual(rectangle.perimeter(10, 54), 128)

    def test_perimeter_3(self):
        self.assertAlmostEqual(rectangle.perimeter(67.636, 42.364), 220)

    def test_area_not_equal(self):
        self.assertNotEqual(rectangle.area(7, 8), 70)

    def test_perimeter_not_equal(self):
        self.assertNotEqual(rectangle.perimeter(10, 54), 120)

    # Негативные тесты
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            rectangle.area(-5, 10)  # Площадь не может быть отрицательной

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-10, 20)  # Периметр не может быть отрицательным

if __name__ == '__main__':
    unittest.main()
