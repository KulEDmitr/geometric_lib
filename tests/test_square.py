import unittest

from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    """
        Тестирование square.py - функции area() и perimeter()
    """

    def test_area_base(self):
        """
            Проверка обычных входных данных - area()
        """
        res = area(10)
        self.assertEqual(res, 100)

        res = area(0)
        self.assertEqual(res, 0)

        res = area(6748749)
        self.assertEqual(res, 45545613065001)

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
        self.assertEqual(res, 100000000000000000000000000000000000000000000000000000000000000000000)

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
        res = perimeter(0, )
        self.assertEqual(res, 0)

        res = perimeter(10)
        self.assertEqual(res, 40)

        res = perimeter(6748749)
        self.assertEqual(res, 26994996)

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
        self.assertEqual(res, 40000000000000000000000000000000000000000000)

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