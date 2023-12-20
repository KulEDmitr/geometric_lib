from triangle import area, perimeter
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
