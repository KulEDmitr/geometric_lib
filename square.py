import unittest

def area(a):
    '''
    Takes square side length, returns value of square area

    Example:
        area(4)
        16
    '''
    if not isinstance(a, int):
        print("Not integer")
        return 0
    if a < 0:
        print("Negative number")
        return 0
    return a * a


def perimeter(a):
    '''
    Takes square side length, returns value of square perimeter

    Example:
        perimeter(3)
        12
    '''
    if not isinstance(a, int):
        print("Not integer")
        return 0
    if a < 0:
        print("Negative number")
        return 0
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_regular_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_str_area(self):
        res = area("a")
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(-2)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_regular_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_str_perimeter(self):
        res = perimeter("a")
        self.assertEqual(res, 0)

    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, 0)
