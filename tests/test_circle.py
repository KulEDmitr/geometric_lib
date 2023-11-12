import math
import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    """
        Тестирование circle.py - функции area() и perimeter()
    """

    def test_area_base(self):
        """
            Проверка обычных входных данных - area()
        """
        res = area(10)
        self.assertEqual(res, math.pi * 100)

        res = area(0)
        self.assertEqual(res, 0)

        res = area(6748749)
        self.assertEqual(res, math.pi * 45545613065001)

    def test_area_negative_values(self):
        """
            Проверка отрицательных чисел, как входных данных - area()
        """
        res = area(-1)
        self.assertEqual(res, ValueError)

    def test_area_big_values(self):
        """
            Проверка больших входных данных - area()
        """
        res = area(10000000000000000000000000000000000)
        self.assertEqual(res, 100000000000000000000000000000000000000000000000000000000000000000000 * math.pi)

    def test_area_types(self):
        """
            Проверка нестандартных типов входных данных - area()
        """
        res = area("test")
        self.assertEqual(res, TypeError)

        res = area([0, 1, 2, 3, 4])
        self.assertEqual(res, TypeError)

        res = area({"test": True})
        self.assertEqual(res, TypeError)

    def test_perimeter_base(self):
        """
            Проверка обычных входных данных - perimeter()
        """
        res = perimeter(0)
        self.assertEqual(res, 0)

        res = perimeter(10)
        self.assertEqual(res, math.pi * 20)

        res = perimeter(987340)
        self.assertEqual(res, math.pi * 1974680)

    def test_perimeter_negative_values(self):
        """
            Проверка отрицательных чисел, как входных данных - perimeter()
        """
        res = perimeter(-1)
        self.assertEqual(res, ValueError)

    def test_perimeter_big_values(self):
        """
            Проверка больших входных данных - perimeter()
        """
        res = perimeter(10000000000000000000000000000000000000000000)
        self.assertEqual(res, math.pi * 20000000000000000000000000000000000000000000)

    def test_perimeter_types(self):
        """
            Проверка нестандартных типов входных данных - perimeter()
        """
        res = perimeter("test")
        self.assertEqual(res, TypeError)

        res = perimeter([0, 1, 2, 3, 4])
        self.assertEqual(res, TypeError)

        res = perimeter({"test": True})
        self.assertEqual(res, TypeError)
