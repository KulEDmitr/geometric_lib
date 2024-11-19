import unittest

def area(a, b):
    return a * b



def perimeter(a, b):
    return 2 * (a + b)

class TestRectangleFunctions(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(4, 0), 0)
        self.assertEqual(area(-2, 3), -6)

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 3), 10)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(4, 0), 8)
        self.assertEqual(perimeter(-2, 3), 2)

if __name__ == '__main__':
    unittest.main()
