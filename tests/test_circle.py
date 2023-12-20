import unittest
from math import pi
from circle import area , perimeter


class MyTestCase(unittest.TestCase):
    def test_normaly_circle_area(self):
        data = area(20)
        self.assertEqual(data , 200 * pi)

    def test_zero_circle_area(self):
        data = area(0)
        self.assertEqual(data , 0)

    def test_string_circle_area(self):
        try:
            data = area('20')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_circle_area(self):
        try:
            data = area(-20)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : negative")

    def test_string_and_int_circle_area(self):
        try:
            data = area("20" , 5)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string and input")


    def test_not_all_elem_circle_area(self):
        with self.assertRaises(TypeError):
            area()

    def test_normaly_circle_perimeter(self):
        data = perimeter(20)
        self.assertEqual(data , 40*pi)

    def test_zero_circle_perimeter(self):
        data = perimeter(0)
        self.assertEqual(data , 0)

    def test_string_circle_perimeter(self):
        try:
            data = perimeter('20')
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : string")

    def test_negative_circle_perimeter(self):
        try:
            data = area(-20)
        except Exception as e:
            data = e.__class__
        self.assertEqual(data , TypeError , "Invalid argumet : negative")

    def test_string_and_int_circle_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter("20", 5)

    def test_not_all_elem_circle_perimeter(self):
        with self.assertRaises(TypeError):
            perimeter()

