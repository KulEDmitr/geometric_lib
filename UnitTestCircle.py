import unittest
from circle import *

'''
Данные тесты проверяют работу функций файла circle.py, проверяя его функции araa и perimetr по 4 раза
'''
class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_big_area(self):
        res = area(10000)
        self.assertEqual(res, 100000000 * math.pi)

    def test_float_area(self):
        res = area(0.5)
        self.assertEqual(res, 0.5*0.5*math.pi)

    def test_string_area(self):
        res = area('10000')
        self.assertEqual(res, 100000000 * math.pi)

    def test_nul_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_big_per(self):
        res = perimeter(10000)
        self.assertEqual(res, 20000 * math.pi)

    def test_float_per(self):
        res = perimeter(0.5)
        self.assertEqual(res, 2*0.5*math.pi)

    def test_string_per(self):
        res = perimeter('10000')
        self.assertEqual(res, 20000 * math.pi)
