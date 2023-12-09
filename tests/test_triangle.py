import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    """
        Тестирование triangle.py - функции area() и perimeter()
    """

    def test_area_base(self):
        """
            Проверка обычных входных данных - area()
        """
        res = area(10, 0)
        self.assertEqual(res, 0)

        res = area(10, 10)
        self.assertEqual(res, 50)

        res = area(6748749, 987340)
        self.assertEqual(res, 3331654918830)

    def test_area_negative_values(self):
        """
            Проверка отрицательных чисел, как входных данных - area()
        """
        res = area(10, -1)
        self.assertEqual(res, ValueError)

        res = area(-10, 1)
        self.assertEqual(res, ValueError)
        res = area(-10, -1)
        self.assertEqual(res, ValueError)

    def test_area_big_values(self):
        """
            Проверка больших входных данных - area()
        """
        res = area(1000000000000000, 1000000000000000)
        self.assertEqual(res, 500000000000000000000000000000)

    def test_area_types(self):
        """
            Проверка нестандартных типов входных данных - area()
        """
        res = area("test", "test")
        self.assertEqual(res, TypeError)

        res = area([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
        self.assertEqual(res, TypeError)

        res = area({"test": True}, {"test": True})
        self.assertEqual(res, TypeError)

    def test_perimeter_base(self):
        """
            Проверка обычных входных данных - perimeter()
        """
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

        res = perimeter(10, 10, 20)
        self.assertEqual(res, 40)

        res = perimeter(6748749, 53468486, 4246346)
        self.assertEqual(res, 64463581)

    def test_perimeter_negative_values(self):
        """
            Проверка отрицательных чисел, как входных данных - perimeter()
        """
        res = perimeter(10, 10, -1)
        self.assertEqual(res, ValueError)

        res = perimeter(-1, 10, 10)
        self.assertEqual(res, ValueError)

        res = perimeter(10, -1, 10)
        self.assertEqual(res, ValueError)

    def test_perimeter_big_values(self):
        """
            Проверка больших входных данных - perimeter()
        """
        res = perimeter(10000000000000000000000000000000000000000000,
                        10000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000)
        self.assertEqual(res, 30000000000000000000000000000000000000000000)

    def test_perimeter_types(self):
        """
            Проверка нестандартных типов входных данных - perimeter()
        """
        res = perimeter("test", "test", "test")
        self.assertEqual(res, TypeError)

        res = perimeter([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
        self.assertEqual(res, TypeError)

        res = perimeter({"test": True}, {"test": True}, {"test": True})
        self.assertEqual(res, TypeError)