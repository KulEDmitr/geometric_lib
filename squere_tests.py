import unittest
import square

class TestStringMethods(unittest.TestCase):

    def test_area_int(self):
        self.assertEqual(square.area(12), 144)

    def test_area_float(self):
        self.assertEqual(square.area(2.5), 6.25)

    def test_area_answer_error(self):
        self.assertNotEqual(square.area(9.0), 81.1)

    def test_area_type_error(self):
        self.assertRaises(TypeError, square.area, 'five')

    def test_perimeter_int(self):
        self.assertEqual(square.perimeter(110), 440)

    def test_perimeter_float(self):
        self.assertEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_answer_error(self):
        self.assertNotEqual(square.perimeter(5.7), 21.1)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, square.perimeter, 'nine', '10')

if __name__ == '__main__':
    unittest.main()
