import unittest
import sys
sys.path.append('C:/Users/Михаил/geometric_lib/functions')
from triangle import area,perimeter
class TestTriangle(unittest.TestCase):
   def test_area_1(self):
       result = area(100, 9)
       self.assertEqual(result, 450)

   def test_area_2(self):
       result = area(-5, 1320)
       self.assertEqual(result, 0)

   def test_area_3(self):
       res = area(1488, 0)
       self.assertEqual(res, 0)
   def test_area_4(self):
       res = area(-1, -1488)
       self.assertEqual(res, 0)




   def test_perimeter_1(self):
       result = perimeter(10, 20, 30)
       self.assertEqual(result, 0)

   def test_perimeter_2(self):
       result = perimeter(3, 4, 5)
       self.assertEqual(result, 12)

   def test_perimeter_3(self):
       res = perimeter(-5, 1488, 1312)
       self.assertEqual(res, 0)
   def test_perimeter_4(self):
       res = perimeter(3, 4, 0)
       self.assertEqual(res, 0)

if __name__ == "__main__":
    unittest.main()
