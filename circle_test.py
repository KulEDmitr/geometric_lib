import unittest
import circle

class TestStringMethods(unittest.TestCase):

    def test_area_int(self):
        self.assertEqual(circle.area(3), 28.274333882308138)

    def test_area_float(self):
        self.assertEqual(circle.area(1.4), 6.157521601035994)

    def test_area_answer_error(self):
        self.assertNotEqual(circle.area(8.65), 16)

    def test_area_type_error(self):
        self.assertRaises(TypeError, circle.area, 'five')

    def test_perimeter_int(self):
        self.assertEqual(circle.perimeter(5), 31.41592653589793)

    def test_perimeter_float(self):
        self.assertEqual(circle.perimeter(2.5), 15.707963267948966)

    def test_perimeter_answer_error(self):
        self.assertNotEqual(circle.perimeter(6.31), 10.2)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, circle.perimeter, 'nine')

if __name__ == '__main__':
    unittest.main()
