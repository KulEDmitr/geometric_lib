import unittest

def area(a, b):
    '''
	Takes rectangle sides length, returns value of rectangle area

	Example:
		area(2, 3)
		6
	'''
    if not isinstance(a, int) or not isinstance(b, int):
        print("Not integer")
        return 0
    if a < 0 or b < 0:
        print("Negative number")
        return 0
    return a * b


def perimeter(a, b):
    '''
	Takes rectangle sides length, returns value of rectangle perimeter

    Example:
        perimeter(2, 5)
        14
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        print("Not integer")
        return 0
    if a < 0 or b < 0:
        print("Negative number")
        return 0
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_regular_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_str_area(self):
        res = area(10, "a")
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(10, -2)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_regular_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_str_perimeter(self):
        res = perimeter(10, "a")
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        res = perimeter(10, -2)
        self.assertEqual(res, 0)
