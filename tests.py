import unittest
import circle
import rectangle
import triangle
import square
import math


class CircleUnitTest(unittest.TestCase):
    def testAreaPi(self):
        self.assertEqual(math.pi, circle.area(1))
    def testPeperimeterPi(self):
        self.assertEqual(2*math.pi, circle.perimeter(1))
    def testInvalidInput(self):
        with self.assertRaises(TypeError):
            circle.area("3")


class RectangleUnitTest(unittest.TestCase):
    def testAreaInt(self):
        self.assertEqual(2*3, rectangle.area(2, 3))
    def testPeperimeter(self):
        self.assertEqual(2*(3 + 4), rectangle.perimeter(3, 4))
    def testInvalidInput(self):
        with self.assertRaises(TypeError):
            rectangle.area("pi", "s")