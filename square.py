import unittest


class SquareTestCase(unittest.TestCase):

    def test_0_area(self):
        area_result = area(0)
        self.assertEqual(area_result, 0)

    def test_1_area(self):
        area_result = area(10)
        self.assertEqual(area_result, 100)

    def test_2_area(self):
        area_result = area(123456789)
        self.assertEqual(area_result, 123456789 ** 2)

    @unittest.expectedFailure
    def test_3_area(self):
        area_result = area("abcd")
        self.assertEqual(area_result, TypeError)

    def test_4_area(self):
        area_result = area(-1)
        self.assertEqual(area_result, TypeError)



    def test_0_perimeter(self):
        perimeter_result = perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_1_perimeter(self):
        perimeter_result = perimeter(10)
        self.assertEqual(perimeter_result, 40)

    def test_2_perimeter(self):
        perimeter_result = perimeter(123456789)
        self.assertEqual(perimeter_result, 4 * 123456789)

    @unittest.expectedFailure
    def test_3_perimeter(self):
        perimeter_result = perimeter("abcd")
        self.assertEqual(perimeter_result, TypeError)

    def test_4_perimeter(self):
        perimeter_result = perimeter(-1)
        self.assertEqual(perimeter_result, TypeError)


def area(a):
    """Принимает на вход сторону квадрата, возвращает площадь данного квадрата."""
    return int(a * a)


def perimeter(a):
    """Принимает на вход сторону квадрата, возвращает периметр данного квадрата."""
    return int(4 * a)


print(area(11))
'''Вывыедет 121, т.к. 11 * 11 = 121.'''

print(perimeter(4))
'''Выведет 16, т.к. 4 * 4 = 16.'''
