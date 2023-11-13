import circle
import rectangle
import square
import triangle
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(circle.CircleTestCase))
    suite.addTest(unittest.makeSuite(rectangle.RectangleTestCase))
    suite.addTest(unittest.makeSuite(square.SquareTestCase))
    suite.addTest(unittest.makeSuite(triangle.TriangleTestCase))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
