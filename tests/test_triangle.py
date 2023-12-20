import unittest
from triangle import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_triangle_area(self):
        data = area(20 , 5)
        self.assertEqual(data , 50)

    def test_zero_triangle_area(self):
        data = area(0 , 20)
        self.assertEqual(data , 0)

    def test_string_triangle_area(self):
        try:
            data = area('20' , '5')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_triangle_area(self):
        try:
            data = area(20 , -5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : negative")

    def test_string_and_int_triangle_area(self):
        with self.assertRaises(TypeError):
            area("20", 5)

    def test_not_all_elem_triangle_area(self):
        with self.assertRaises(TypeError):
            area(5)

    def test_normaly_triangle_perimeter(self):
        data = perimeter(3 , 4 , 5)
        self.assertEqual(data , 12)

    def test_zero_triangle_perimeter(self):
        data = perimeter(0 , 0 , 0)
        self.assertEqual(data , 0)

    def test_string_triangle_perimeter(self):
        try:
            data = perimeter('20' , '5', '7')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Invalid argumet : string")

    def test_negative_triangle_perimeter(self):
        try:
            data = perimeter(20, -5 , 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data, TypeError, "Invalid argumet : negative")

    def test_string_and_int_triangle_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("20", 5, 3)

    def test_not_all_elem_triangle_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter(20, 5)

