import unittest
from rectangle import *


class RectangleTestCase(unittest.TestCase):
	def test_area_zero(self):
		a, b = 5, 0
		answer = 0
		res = area(a, b)
		self.assertEqual(res, answer)

	def test_area_float(self):
		a, b, = 5.1, 6.8
		answer = 34.68
		res = area(a, b)
		self.assertAlmostEqual(res, answer)

	def test_area_both_negative(self):
		a, b = -5, -5
		error = ValueError
		with self.assertRaises(error):
			area(a, b)

	def test_area_first_negative(self):
		a, b = -5, 5
		error = ValueError
		with self.assertRaises(error):
			area(a, b)

	def test_area_second_negative(self):
		a, b = 5, -5
		error = ValueError
		with self.assertRaises(error):
			area(a, b)

	def test_area_both_string(self):
		a, b = "string", "string"
		answer = TypeError
		with self.assertRaises(answer):
			area(a, b)
	
	def test_area_first_string(self):
		a, b = "string", 5
		error = TypeError
		with self.assertRaises(error):
			area(a, b)

	def test_area_second_string(self):
		a, b = 5, "string"
		error = TypeError
		with self.assertRaises(error):
			area(a, b)

	def test_perimeter_zero(self):
		a, b = 5, 0
		answer = 5
		res = perimeter(a, b)
		self.assertEqual(res, answer)

	def test_perimeter_float(self):
		a, b = 5.1, 6.8
		answer = 23.8
		res = perimeter(a, b)
		self.assertAlmostEqual(res, answer)

	def test_perimeter_both_negative(self):
		a, b = -5, -5
		error = ValueError
		with self.assertRaises(error):
			perimeter(a, b)

	def test_perimeter_first_negative(self):
		a, b = -5, 5
		error = ValueError
		with self.assertRaises(error):
			perimeter(a, b)

	def test_perimeter_second_negative(self):
		a, b = 5, -5
		error = ValueError
		with self.assertRaises(error):
			perimeter(a, b)

	def test_perimeter_both_string(self):
		a, b = "string", "string"
		error = TypeError
		with self.assertRaises(error):
			perimeter(a, b)

	def test_perimeter_first_string(self):
		a, b = "string", 5
		error = TypeError
		with self.assertRaises(error):
			perimeter(a, b)

	def test_perimeter_second_string(self):
		a, b = 5, "string"
		error = TypeError
		with self.assertRaises(error):
			perimeter(a, b)
