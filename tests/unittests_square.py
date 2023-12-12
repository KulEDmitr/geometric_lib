import unittest

from src.square import area
from src.square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_sq_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_sq_area_neg(self):
        res = area(-1)
        self.assertEqual(res, "Incorrect input")

    def test_sq_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
    def test_sq_area_neg(self):
        res = perimeter(-1)
        self.assertEqual(res, "Incorrect input")

    def test_sq_area(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_sq_area_big(self):
        res = area(212345)
        self.assertEqual(res, 45090399025)

    def test_sq_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_sq_perimeter_big(self):
        res = perimeter(212345)
        self.assertEqual(res, 849380)
        
if __name__ == '__main__':
    import xmlrunner
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
