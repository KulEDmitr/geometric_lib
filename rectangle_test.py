import unittest
import rectangle

class TestStringMethods(unittest.TestCase):

    def test_area_int(self):
        self.assertEqual(rectangle.area(7, 7), 49)

    def test_area_float(self):
        self.assertEqual(rectangle.area(2.4, 3.65), 8.76)

    def test_area_answer_error(self):
        self.assertNotEqual(rectangle.area(8.65, 4.183), 8)

    def test_area_type_error(self):
        self.assertRaises(TypeError, rectangle.area, 'nine', '7')

    def test_perimeter_int(self):
        self.assertEqual(rectangle.perimeter(12, 3), 30)

    def test_perimeter_float(self):
        self.assertEqual(rectangle.perimeter(2.25, 1.0), 6.5)

    def test_perimeter_answer_error(self):
        self.assertNotEqual(rectangle.perimeter(18, 3), 41)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, rectangle.perimeter, 'abc', 9)

if __name__ == '__main__':
    unittest.main()
