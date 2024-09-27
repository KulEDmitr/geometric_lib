from triangle import area, perimeter
import unittest


class TriangleTestCase(unittest.TestCase):

	def test_0_area(self):
		area_result = area(11, 0)
		self.assertEqual(area_result, 0)

	def test_1_area(self):
		area_result = area(123456789, 9876543210)
		self.assertEqual(area_result, (123456789 * 9876543210) / 2)


	def test_0_perimeter(self):
		perimeter_result = perimeter(0, 0, 0)
		self.assertEqual(perimeter_result, 0)

	def test_1_perimeter(self):
		perimeter_result = perimeter(123456789, 9876543210, 1)
		self.assertEqual(perimeter_result, 123456789 + 9876543210 + 1)
