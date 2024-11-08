import unittest
from rectangle import *

'''
Данные тесты проверяют работу функций файлаrectangle.py, проверяя его функции araa и perimetr по 2 раза
'''
class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0,0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(10000,10000)
        self.assertEqual(res, 100000000)

    def test_nul_per(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_big_per(self):
        res = perimeter(10000, 10000)
        self.assertEqual(res, 40000)