import unittest


class TriangleTestCase(unittest.TestCase):

	def test_0_area(self):
		area_result = area(11, 0)
		self.assertEqual(area_result, 0)

	def test_1_area(self):
		area_result = area(123456789, 9876543210)
		self.assertEqual(area_result, (123456789 * 9876543210) / 2)

	@unittest.expectedFailure
	def test_2_area(self):
		area_result = area("abcd", 1)
		self.assertEqual(area_result, TypeError)

	@unittest.expectedFailure
	def test_3_area(self):
		area_result = area("ab", "cd")
		self.assertEqual(area_result, TypeError)

	def test_4_area(self):
		area_result = area(11, -1)
		self.assertEqual(area_result, TypeError)




	def test_0_perimeter(self):
		perimeter_result = perimeter(0, 0, 0)
		self.assertEqual(perimeter_result, 0)

	def test_1_perimeter(self):
		perimeter_result = perimeter(123456789, 9876543210, 1)
		self.assertEqual(perimeter_result, 123456789 + 9876543210 + 1)

	def test_2_perimeter(self):
		perimeter_result = perimeter("a", "b", "c")
		self.assertEqual(perimeter_result, TypeError)

	@unittest.expectedFailure
	def test_3_perimeter(self):
		perimeter_result = perimeter("a", 2, "c")
		self.assertEqual(perimeter_result, TypeError)

	def test_4_perimeter(self):
		perimeter_result = perimeter(1, -2, 3)
		self.assertEqual(perimeter_result, TypeError)


def area(a, h):
	"""Принимает на вход основание и высоту треугольника, возвращает площадь данного треугольника."""
	return a * h / 2


def perimeter(a, b, c):
	"""Принимает на вход 3 стороны треугольника, возвращает периметр данного треугольника."""
	return a + b + c


print(area(5, 4))
'''Выведет 10, т.к. 5 * 4 / 2 = 10.'''

print(perimeter(6, 8, 10))
'''Выведет 24, т.к. 6 + 8 + 10 = 24.'''
