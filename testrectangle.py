import unittest
from rectangle import area , perimeter

class RectangleTestCase(unittest.TestCase):
    def test_0_area(self):
       res = area(10, 0)
       self.assertEqual(res, 0)

    def test_1_area(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_2_area(self):
       res = area(200_000_000,200_000_000_000_000_000)
       self.assertEqual(res,200_000_000*200_000_000_000_000_000)

    @unittest.expectedFailure
    def test_wrong_input_1_area(self):
       res = area("a",'b')
       self.assertEqual(res)


    def test_wrong_input_2_area(self):
       res = area("a",2)
       self.assertEqual(res,TypeError)

    def test_1_perimeter(self):
       res = perimeter(0,0)
       self.assertEqual(res,0)

    def test_2_perimeter(self):
       res = perimeter(10,20)
       self.assertEqual(res,60) 

    def test_3_perimeter(self):
       res = perimeter(100_000_000_00,200_000_000)
       self.assertEqual(res,2*(10000000000+200000000))


    

    @unittest.expectedFailure
    def test_5_perimeter_wrong_input(self):
       res = perimeter("a",'b')
       self.assertEqual(res)