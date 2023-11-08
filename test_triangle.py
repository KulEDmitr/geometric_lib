import unittest
from triangle import *


class TriangleTestCase(unittest.TestCase):
	def test_perimeter_zero(self):
		a, b, c = 0, 0, 0
		answer = 0
		res = perimeter(a, b, c)
		self.assertEqual(res, answer)

	def test_perimeter_float(self):
		a, b, c = 5.1, 6.87, 4.14
		answer = 16.11
		res = perimeter(a, b, c)
		self.assertAlmostEqual(res, answer)

	def test_perimeter_with_negative(self):
		variants = [123, -123]
		error = ValueError

		for a in variants:
			for b in variants:
				for c in variants:
					if min(a,b,c) >= 0:
						continue
					with self.assertRaises(error):
						perimeter(a, b, c)

	def test_perimeter_with_string(self):
		variants = [123, "string"]
		error = TypeError

		for a in variants:
			for b in variants:
				for c in variants:
					if (a == b == c == variants[0]):
						continue
					with self.assertRaises(error):
						perimeter(a, b, c)

	def test_area_zero(self):
		a, h = 10, 0
		answer = 0
		res = area(a, h)
		self.assertEqual(res, answer)

	def test_area_float(self):
		a, h = 10.123, 6.312
		answer = 31.948188
		res = area(a, h)
		self.assertAlmostEqual(res, answer)

	def test_area_with_negative(self):
		variants = [10, -10]
		error = ValueError

		for a in variants:
			for h in variants:
				if min(a, h) >= 0:
					continue

				with self.assertRaises(error):
					area(a, h)

	def test_area_with_string(self):
		variants = [10, "string"]
		error = TypeError

		for a in variants:
			for h in variants:
				if a == h == variants[0]:
					continue

				with self.assertRaises(error):
					area(a, h)