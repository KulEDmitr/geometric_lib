import unittest
import square

class SquareTestCase(unittest.TestCase):

    def test_area_1(self):
        self.assertEqual(square.area(0), 0)

    def test_area_2(self):
        self.assertEqual(square.area(10), 100)

    def test_area_3(self):
        self.assertAlmostEqual(square.area(8.5), 72.25)

    def test_perimeter_1(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_2(self):
        self.assertEqual(square.perimeter(10), 40)

    def test_perimeter_3(self):
        self.assertAlmostEqual(square.perimeter(17.25), 69)

    def test_area_not_equal(self):
        self.assertNotEqual(square.area(10), 40)  # Площадь не должна быть равна 40

    def test_perimeter_not_equal(self):
        self.assertNotEqual(square.perimeter(10), 30)  # Периметр не должен быть равен 30

    # Негативные тесты
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            square.area(-5)  # Площадь не может быть отрицательной

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            square.perimeter(-10)  # Периметр не может быть отрицательным

if __name__ == '__main__':
    unittest.main()
