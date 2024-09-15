import unittest
import triangle

class TestStringMethods(unittest.TestCase):

    def test_area_int(self):
        self.assertEqual(triangle.area(3, 4), 6.0)

    def test_area_float(self):
        self.assertEqual(triangle.area(1.4, 0), 0)

    def test_area_answer_error(self):
        self.assertNotEqual(triangle.area(8.65, 4.183), 8)

    def test_area_type_error(self):
        self.assertRaises(TypeError, triangle.area, 'two', 8)

    def test_perimeter_int(self):
        self.assertEqual(triangle.perimeter(110, 15, 6), 131)

    def test_perimeter_float(self):
        self.assertEqual(triangle.perimeter(2.25, 1.0, 2.7), 5.95)

    def test_perimeter_answer_error(self):
        self.assertNotEqual(triangle.perimeter(6.31, 4, 5.7), 10.2)

    def test_perimeter_type_error(self):
        self.assertRaises(TypeError, triangle.perimeter, 'eleven', 9, 12.5)

if __name__ == '__main__':
    unittest.main()
