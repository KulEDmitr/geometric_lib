from rectangle import area, perimeter, diagonal
import unittest


class RectangleTestCase(unittest.TestCase):

    def test_0_area(self):
        area_result = area(0, 1)
        self.assertEqual(area_result, 0)

    def test_1_area(self):
        area_result = area(5, 5)
        self.assertEqual(area_result, 25)

    def test_2_area(self):
        area_result = area(123456789, 987654321)
        self.assertEqual(area_result, 123456789 * 987654321)

    @unittest.expectedFailure
    def test_3_area(self):
        area_result = area("ab", "cd")
        self.assertEqual(area_result, TypeError)

    @unittest.expectedFailure
    def test_4_area(self):
        area_result = area("abcd", 123456789)
        self.assertEqual(area_result, TypeError)

    def test_5_area(self):
        area_result = area(-1, 123456789)
        self.assertEqual(area_result, TypeError)



    def test_0_perimeter(self):
        perimeter_result = perimeter(0, 1)
        self.assertEqual(perimeter_result, 2)

    def test_1_perimeter(self):
        perimeter_result = perimeter(5, 10)
        self.assertEqual(perimeter_result, 30)

    def test_2_perimeter(self):
        perimeter_result = perimeter(123456789, 987654321)
        self.assertEqual(perimeter_result, 2 * (123456789 + 987654321))

    @unittest.expectedFailure
    def test_3_perimeter(self):
        perimeter_result = perimeter("abcd", 2)
        self.assertEqual(perimeter_result, TypeError)

    @unittest.expectedFailure
    def test_4_perimeter(self):
        perimeter_result = perimeter("ab", "cd")
        self.assertEqual(perimeter_result, TypeError)

    def test_5_perimeter(self):
        perimeter_result = area(-1, 123456789)
        self.assertEqual(perimeter_result, TypeError)



    def test_0_diagonal(self):
        diagonal_result = diagonal(3, 4)
        self.assertEqual(diagonal_result, 5)

    def test_1_diagonal(self):
        diagonal_result = diagonal(6, 8)
        self.assertEqual(diagonal_result, 10)

    def test_2_diagonal(self):
        diagonal_result = diagonal(123456789, 987654321)
        self.assertEqual(diagonal_result, (123456789 ** 2 + 987654321 ** 2) ** 0.5)

    def test_3_diagonal(self):
        diagonal_result = diagonal(-1, 123456789)
        self.assertEqual(diagonal_result, TypeError)