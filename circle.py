import unittest
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

class TestCircleFunctions(unittest.TestCase):

    def test_area(self): 
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(0), 0)
        self.assertAlmostEqual(area(2), 4 * math.pi)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(0), 0)
        self.assertAlmostEqual(perimeter(2), 4 * math.pi)

if __name__ == '__main__':
    unittest.main()
