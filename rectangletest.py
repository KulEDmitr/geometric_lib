import unittest
from rectangle import area, perimeter

class test_rectangle_area(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 2), 6)
        self.assertEqual(area(4, 3), 12)
        self.assertEqual(area(5, 4), 20)
        self.assertEqual(area(6, 5), 30)
    def exception_test_area(self):
        self.assertEqual(area(15,0), 0)
        self.assertEqual(area(0,15), 0)
        self.assertEqual(area(0,0), 0)
        self.assertEqual(area(-3,2), 0)
        self.assertEqual(area(3,-2), 0)
        self.assertEqual(area(-2,0), 0)
    def unexpected_types_test_area(self):
        self.assertEqual(area("3","2"), 6)
        self.assertEqual(area("4","3"), 12)
        self.assertEqual(area("5","4"), 20)
        self.assertEqual(area("6","5"), 30)
        self.assertEqual(area([3],[2]), 6)
        self.assertEqual(area([4],[3]), 12)
        self.assertEqual(area([5],[4]), 20)
        self.assertEqual(area([6],[5]), 30)
    def overflow_test_area(self):
        self.assertEqual(area(63242397497234343,358628652387652387), 22680535788197392507601354962326741)
    def unexpected_types_of_exceptions_test_area(self):
        self.assertEqual(area("15","0"), 0)
        self.assertEqual(area("0","15"), 0)
        self.assertEqual(area("0","0"), 0)
        self.assertEqual(area("-3","2"), 0)
        self.assertEqual(area("3","-2"), 0)
        self.assertEqual(area("-2","0"), 0)
        self.assertEqual(area([15], [0]), 0)
        self.assertEqual(area([0], [15]), 0)
        self.assertEqual(area([0], [0]), 0)
        self.assertEqual(area([-3], [2]), 0)
        self.assertEqual(area([3], [-2]), 0)
        self.assertEqual(area([-2], [0]), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(3, 2), 10)
        self.assertEqual(perimeter(4, 3), 14)
        self.assertEqual(perimeter(5, 4), 18)
        self.assertEqual(perimeter(6, 5), 22)
class test_rectangle_perimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 2), 10)
        self.assertEqual(perimeter(4, 3), 14)
        self.assertEqual(perimeter(5, 4), 18)
        self.assertEqual(perimeter(6, 5), 22)
    def exception_test_perimeter(self):
        self.assertEqual(perimeter(15,0), 0)
        self.assertEqual(perimeter(0,15), 0)
        self.assertEqual(perimeter(0,0), 0)
        self.assertEqual(perimeter(-3,2), 0)
        self.assertEqual(perimeter(3,-2), 0)
        self.assertEqual(perimeter(-2,0), 0)
    def unexpected_types_test_perimeter(self):
        self.assertEqual(perimeter("3","2"), 10)
        self.assertEqual(perimeter("4","3"), 14)
        self.assertEqual(perimeter("5","4"), 18)
        self.assertEqual(perimeter("6","5"), 22)
        self.assertEqual(perimeter([3],[2]), 10)
        self.assertEqual(perimeter([4],[3]), 14)
        self.assertEqual(perimeter([5],[4]), 18)
        self.assertEqual(perimeter([6],[5]), 22)
    def overflow_test_perimeter(self):
        self.assertEqual(perimeter(63242397497234343,358628652387652387), 843742099769773460)
    def unexpected_types_of_exceptions_test_perimeter(self):
        self.assertEqual(perimeter("15","0"), 0)
        self.assertEqual(perimeter("0","15"), 0)
        self.assertEqual(perimeter("0","0"), 0)
        self.assertEqual(perimeter("-3","2"), 0)
        self.assertEqual(perimeter("3","-2"), 0)
        self.assertEqual(perimeter("-2","0"), 0)
