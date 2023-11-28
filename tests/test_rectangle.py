import unittest
import sys
sys.path.append('C:/Users/Михаил/geometric_lib/functions')
from rectangle import area, perimeter
class TestRectangle(unittest.TestCase):
   def test_area_1(self):
       result = area(10, 9)
       self.assertEqual(result, 90)
   def test_area_2(self):
       result = area(-52, 10)
       self.assertEqual(result, 0)
   def test_area_3(self):
       res = area(1488, 0)
       self.assertEqual(res, 0)
   def test_area_4(self):
       res = area(-1488, -10)
       self.assertEqual(res, 0)


       
   def test_perimeter_1(self):
       result = perimeter(1, 9)
       self.assertEqual(result, 20)
   def test_perimeter_2(self):
       result = perimeter(-56, 10)
       self.assertEqual(result, 0)
   def test_perimeter_3(self):
       res = perimeter(136, 0)
       self.assertEqual(res, 0)
   def test_perimeter_4(self):
       res = perimeter(-1488, -10)
       self.assertEqual(res, 0)
if __name__ == "__main__":
    unittest.main()
