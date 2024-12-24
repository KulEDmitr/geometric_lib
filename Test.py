import unittest
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle_lab import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class ContinueTestResult(unittest.TestResult):
    def addFailure(self, test, err):
        super().addFailure(test, err)


class TestCircle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertAlmostEqual(circle_area(2), 12.56637061)  # Тест с целым числом
        except AssertionError as e:
            print(f"Circle area test 1 failed: {e}")

        try:
            self.assertAlmostEqual(circle_area(1.5), 7.06858347)  # Тест с дробным числом
        except AssertionError as e:
            print(f"Circle area test 2 failed: {e}")

        try:
            self.assertEqual(circle_area(0), 0)  # Тест с нулевым радиусом
        except AssertionError as e:
            print(f"Circle area test 3 failed: {e}")

    def test_perimeter(self):
        try:
            self.assertAlmostEqual(circle_perimeter(3), 18.84955592)  # Тест с целым числом
        except AssertionError as e:
            print(f"Circle perimeter test 1 failed: {e}")

        try:
            self.assertAlmostEqual(circle_perimeter(2.5), 15.70796326)  # Тест с дробным числом
        except AssertionError as e:
            print(f"Circle perimeter test 2 failed: {e}")

        try:
            self.assertEqual(circle_perimeter(0), 0)  # Тест с нулевым радиусом
        except AssertionError as e:
            print(f"Circle perimeter test 3 failed: {e}")


class TestRectangle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(rectangle_area(2, 3), 6)  # Тест с целыми числами
        except AssertionError as e:
            print(f"Rectangle area test 1 failed: {e}")

        try:
            self.assertEqual(rectangle_area(1.5, 2.5), 3.75)  # Тест с дробными числами
        except AssertionError as e:
            print(f"Rectangle area test 2 failed: {e}")

        try:
            self.assertEqual(rectangle_area(0, 5), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Rectangle area test 3 failed: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(rectangle_perimeter(2, 3), 10)  # Тест с целыми числами
        except AssertionError as e:
            print(f"Rectangle perimeter test 1 failed: {e}")

        try:
            self.assertAlmostEqual(rectangle_perimeter(1.5, 2.5), 8)  # Тест с дробными числами
        except AssertionError as e:
            print(f"Rectangle perimeter test 2 failed: {e}")

        try:
            self.assertEqual(rectangle_perimeter(0, 5), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Rectangle perimeter test 3 failed: {e}")


class TestSquare(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(square_area(2), 4)  # Тест с целым числом
        except AssertionError as e:
            print(f"Square area test 1 failed: {e}")

        try:
            self.assertAlmostEqual(square_area(1.5), 2.25)  # Тест с дробным числом
        except AssertionError as e:
            print(f"Square area test 2 failed: {e}")

        try:
            self.assertEqual(square_area(0), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Square area test 3 failed: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(square_perimeter(2), 8)  # Тест с целым числом
        except AssertionError as e:
            print(f"Square perimeter test 1 failed: {e}")

        try:
            self.assertAlmostEqual(square_perimeter(1.5), 6)  # Тест с дробным числом
        except AssertionError as e:
            print(f"Square perimeter test 2 failed: {e}")

        try:
            self.assertEqual(square_perimeter(0), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Square perimeter test 3 failed: {e}")


class TestTriangle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(triangle_area(3, 4), 6)  # Тест с целыми числами
        except AssertionError as e:
            print(f"Triangle area test 1 failed: {e}")

        try:
            self.assertAlmostEqual(triangle_area(2.5, 3.5), 4.375)  # Тест с дробными числами
        except AssertionError as e:
            print(f"Triangle area test 2 failed: {e}")

        try:
            self.assertEqual(triangle_area(0, 5), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Triangle area test 3 failed: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(triangle_perimeter(3, 5, 7), 15)  # Тест с целыми числами
        except AssertionError as e:
            print(f"Triangle perimeter test 1 failed: {e}")

        try:
            self.assertEqual(triangle_perimeter(2.5, 3.5, 1.0), 7)  # Тест с дробными числами
        except AssertionError as e:
            print(f"Triangle perimeter test 2 failed: {e}")

        try:
            self.assertEqual(triangle_perimeter(0, 5, 6), 0)  # Тест с нулевой стороной
        except AssertionError as e:
            print(f"Triangle perimeter test 3 failed: {e}")


if __name__ == '__main__':
    test_runner = unittest.TextTestRunner(resultclass=ContinueTestResult)
    unittest.main(testRunner=test_runner)