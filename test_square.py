import unittest
from square import *


class SquareTestCase(unittest.TestCase):
	def test_area_zero(self):
		a = 0
		answer = 0
		res = area(a)
		self.assertEqual(res, answer)

	def test_area_float(self):
		a = 5.123
		answer = 26.245129
		res = area(a)
		self.assertAlmostEqual(res, answer)

	def test_area_negative(self):
		a = -5
		error = ValueError
		with self.assertRaises(error):
			area(a)

	def test_area_string(self):
		a = "string"
		error = TypeError
		with self.assertRaises(error):
			area(a)

	def test_perimeter_zero(self):
		a = 0
		answer = a
		res = perimeter(a)
		self.assertEqual(res, answer)

	def test_perimeter_float(self):
		a = 5.123
		answer = 20.492
		res = perimeter(a)
		self.assertAlmostEqual(res, answer)

	def test_perimeter_negative(self):
		a = -5
		error = ValueError
		with self.assertRaises(error):
			perimeter(a)

	def test_perimeter_string(self):
		a = "string"
		error = TypeError
		with self.assertRaises(error):
			perimeter(a)
