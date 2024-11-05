import unittest

def area(a, h):
    '''
    Takes lengths of the triangle side and triangle height, returns area of the triangle

    Example:
        area(3, 4)
        6
    '''
    if not isinstance(a, int) or not isinstance(h, int):
        print("Not integer")
        return 0
    if a < 0 or h < 0:
        print("Negative number")
        return 0
    return a * h / 2

def perimeter(a, b, c):
    '''
    Takes lengths of the triangle sides, returns perimeter of the triangle

    Example:
        perimeter(3, 2, 5)
        10
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        print("Not integer")
        return 0
    if a < 0 or b < 0 or c < 0:
        print("Negative number")
        return 0
    return a + b + c


class TriangleTestCase(unittest.TestCase):
	def test_zero_area(self):
		res = area(10, 0)
		self.assertEqual(res, 0)

	def test_regular_area(self):
		res = area(5, 3)
		self.assertEqual(res, 7.5)

	def test_str_area(self):
		res = area(10, "a")
		self.assertEqual(res, 0)

	def test_negative_area(self):
		res = area(10, -2)
		self.assertEqual(res, 0)

	def test_zero_perimeter(self):
		res = perimeter(10, 0, 4)
		self.assertEqual(res, 14)

	def test_regular_perimeter(self):
		res = perimeter(10, 5, 7)
		self.assertEqual(res, 22)

	def test_str_perimeter(self):
		res = perimeter(10, "a", 3)
		self.assertEqual(res, 0)

	def test_negative_perimeter(self):
		res = perimeter(10, -2, 5)
		self.assertEqual(res, 0)
