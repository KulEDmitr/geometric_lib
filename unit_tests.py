import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rect_area(5, 10), 50)
        self.assertEqual(rect_area(0, 10), 0)
        self.assertEqual(rect_area(0, -10), 0)


    def test_perimeter(self):
        self.assertEqual(rect_perimeter(5, 10), 30)
        self.assertEqual(rect_perimeter(0, 10), 20)




class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(0), 0)


    def test_perimeter(self):
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(0), 0)



class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle_area(3, 4), 6)
        self.assertEqual(triangle_area(0, 4), 0)
        self.assertEqual(triangle_area(-3,4), 0)


    def test_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4), 12)
        self.assertEqual(triangle_perimeter(0, 4), 0)
        self.assertEqual(triangle_perimeter(-3, 4), 0)



class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(5), 78.54, places=2)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(-5), 0)


    def test_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(5), 31.42, places=2)
        self.assertEqual(circle_perimeter(0), 0)
        self.assertEqual(circle_perimeter(-5), 0)


if __name__ == "__main__":
    unittest.main()


"""""""""
import unittest
from rectangle import area as rect_area, perimeter as rect_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter


class TestRectangle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(rect_area(5, 10), 50)
        except Exception as e:
            self.fail(f"rect_area(5, 10) raised an exception: {e}")

        try:
            self.assertEqual(rect_area(0, 10), 0)
        except Exception as e:
            self.fail(f"rect_area(0, 10) raised an exception: {e}")

        try:
            self.assertEqual(rect_area(5, -10), 0)
        except Exception as e:
            self.fail(f"rect_area(5, -10) raised an exception: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(rect_perimeter(5, 10), 30)
        except Exception as e:
            self.fail(f"rect_perimeter(5, 10) raised an exception: {e}")

        try:
            self.assertEqual(rect_perimeter(0, 10), 20)
        except Exception as e:
            self.fail(f"rect_perimeter(0, 10) raised an exception: {e}")


class TestSquare(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(square_area(5), 25)
        except Exception as e:
            self.fail(f"square_area(5) raised an exception: {e}")

        try:
            self.assertEqual(square_area(0), 0)
        except Exception as e:
            self.fail(f"square_area(0) raised an exception: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(square_perimeter(5), 20)
        except Exception as e:
            self.fail(f"square_perimeter(5) raised an exception: {e}")

        try:
            self.assertEqual(square_perimeter(0), 0)
        except Exception as e:
            self.fail(f"square_perimeter(0) raised an exception: {e}")


class TestTriangle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertEqual(triangle_area(3, 4), 6)
        except Exception as e:
            self.fail(f"triangle_area(3, 4) raised an exception: {e}")

        try:
            self.assertEqual(triangle_area(0, 4), 0)
        except Exception as e:
            self.fail(f"triangle_area(0, 4) raised an exception: {e}")

        try:
            self.assertEqual(triangle_area(-3, 4), 0)
        except Exception as e:
            self.fail(f"triangle_area(-3, 4) raised an exception: {e}")

    def test_perimeter(self):
        try:
            self.assertEqual(triangle_perimeter(3, 4), 12)
        except Exception as e:
            self.fail(f"triangle_perimeter(3, 4) raised an exception: {e}")

        try:
            self.assertEqual(triangle_perimeter(0, 4), 0)
        except Exception as e:
            self.fail(f"triangle_perimeter(0, 4) raised an exception: {e}")

        try:
            self.assertEqual(triangle_perimeter(-3, 4), 0)
        except Exception as e:
            self.fail(f"triangle_perimeter(-3, 4) raised an exception: {e}")


class TestCircle(unittest.TestCase):
    def test_area(self):
        try:
            self.assertAlmostEqual(circle_area(5), 78.54, places=2)
        except Exception as e:
            self.fail(f"circle_area(5) raised an exception: {e}")

        try:
            self.assertEqual(circle_area(0), 0)
        except Exception as e:
            self.fail(f"circle_area(0) raised an exception: {e}")

        try:
            self.assertEqual(circle_area(-5), 0)
        except Exception as e:
            self.fail(f"circle_area(-5) raised an exception: {e}")

    def test_perimeter(self):
        try:
            self.assertAlmostEqual(circle_perimeter(5), 31.42, places=2)
        except Exception as e:
            self.fail(f"circle_perimeter(5) raised an exception: {e}")

        try:
            self.assertEqual(circle_perimeter(0), 0)
        except Exception as e:
            self.fail(f"circle_perimeter(0) raised an exception: {e}")

        try:
            self.assertEqual(circle_perimeter(-5), 0)
        except Exception as e:
            self.fail(f"circle_perimeter(-5) raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
"""""""""
