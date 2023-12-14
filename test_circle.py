import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
	def test_area_zero(self):
		radius = 0
		answer = 0
		res = area(radius)
		self.assertEqual(res, answer)

	def test_area_float(self):
		radius = 5.1
		answer = 81.7128249198705
		res = area(radius)
		self.assertAlmostEqual(res, answer)

	def test_area_negative(self):
		radius = -0.23
		error = ValueError
		with self.assertRaises(error):
			area(radius)

	def test_area_string(self):
		radius = "123"
		error = TypeError
		with self.assertRaises(error):
			area(radius)

	def test_perimeter_zero(self):
		radius = 0
		answer = 0
		res = perimeter(radius)
		self.assertEqual(res, answer)

	def test_perimeter_float(self):
		radius = 4.2
		answer = 26.389378290154262
		res = perimeter(radius)
		self.assertAlmostEqual(res, answer)

	def test_perimeter_negative(self):
		radius = -102
		error = ValueError
		with self.assertRaises(error):
			perimeter(radius)

	def test_perimeter_string(self):
		radius = "string"
		error = TypeError
		with self.assertRaises(error):
			perimeter(radius)