import unittest
from square import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_square_area(self):
        data = area(20)
        self.assertEqual(data , 200)

    def test_zero_square_area(self):
        data = area(0)
        self.assertEqual(data , 0)

    def test_string_square_area(self):
        try:
            data = area('20')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_square_area(self):
        try:
            data = area(-10)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Invalid argumet : negative")

    def test_string_and_int_square_area(self):
        with self.assertRaises(TypeError):
            area("20", 5)

    def test_not_all_elem_square_area(self):
        with self.assertRaises(TypeError):
            area()

    def test_normaly_square_perimeter(self):
        data = perimeter(20)
        self.assertEqual(data , 80)

    def test_zero_square_perimeter(self):
        data = perimeter(0)
        self.assertEqual(data , 0)

    def test_string_square_perimeter(self):
        try:
            data = perimeter('20')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_square_perimeter(self):
        try:
            data = perimeter(-20)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Invalid argumet : negative")

    def test_string_and_int_square_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("20", 5)

    def test_not_all_elem_square_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter()


