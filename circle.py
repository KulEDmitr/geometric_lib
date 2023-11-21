import unittest
from math import pi


class CircleTestCase(unittest.TestCase):

    def test_0_area(self):
        area_result = area(0)
        self.assertEqual(area_result, 0)

    def test_1_area(self):
        area_result = area(123)
        self.assertEqual(area_result, pi * (123 ** 2))

    @unittest.expectedFailure
    def test_2_area(self):
        area_result = area("abcd")
        self.assertEqual(area_result, TypeError)

    def test_3_area(self):
        area_result = area(-99)
        self.assertEqual(area_result, TypeError)



    def test_0_perimeter(self):
        perimeter_result = perimeter(0)
        self.assertEqual(perimeter_result, 0)

    def test_1_perimeter(self):
        perimeter_result = perimeter(123)
        self.assertEqual(perimeter_result, 2 * pi * 123)

    @unittest.expectedFailure
    def test_2_perimeter(self):
        perimeter_result = perimeter("abcd")
        self.assertEqual(perimeter_result, TypeError)

    def test_3_perimeter(self):
        perimeter_result = perimeter(-99)
        self.assertEqual(perimeter_result, TypeError)


def area(r):
<<<<<<< HEAD
    """Принимает на вход радиус круга, возвращает площадь данного круга."""
    return pi * r * r


def perimeter(r):
    """Принимает на вход радиус круга, возвращает периметр данного круга."""
    return 2 * pi * r
=======
    '''Принимает на вход радиус круга, возвращает площадь данного круга.
    print(area(7)) Выведет 153.93804002589985, т.к. π * 7 * 7 ≈ 153.93804...'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает на вход радиус круга, возвращает периметр данного круга.
    print(perimeter(10)) Выведет 62.83185307179586, т.к. 2 * 10 * π ≈ 62.83185...'''
    return 2 * math.pi * r
>>>>>>> 84b77868fc420ea243df4eddbf4cf38ccf9903c0





