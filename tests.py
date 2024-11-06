import unittest
import math

import square
import triangle
import rectangle
import circle

class TestGeometryFunctions(unittest.TestCase):

        '''square'''
        def test_square_area(self):
            self.assertEqual(square.area(4), 16)
            self.assertEqual(square.area(0), 0)
            self.assertEqual(square.area(-2.5), 0)
            with self.assertRaises(TypeError):
                square.area("string")

        def test_square_perimeter(self):
            self.assertEqual(square.perimeter(4), 16)
            self.assertEqual(square.perimeter(0), 0)
            self.assertEqual(square.perimeter(-2.5), 0)
            with self.assertRaises(TypeError):
                square.perimeter("string")

    
        '''triangle'''
        def test_triangle_area(self):
            self.assertEqual(triangle.area(4 , 5 ), 10)
            self.assertEqual(triangle.area(0 , 4), 0)
            self.assertEqual(triangle.area(-10 , -10), 0)
            with self.assertRaises(TypeError):
                triangle.area("string")

        def test_triangle_perimeter(self):
            self.assertEqual(triangle.perimeter(4 , 3 , 2), 9)
            self.assertEqual(triangle.perimeter(0 , 3 , 5), 0)
            self.assertEqual(triangle.perimeter(-2.5 , 2.5 , 5), 0)
            with self.assertRaises(TypeError):
                triangle.perimeter("string")
            
        '''rectangle'''    
        def test_rectangle_area(self):
            self.assertEqual(rectangle.area(3 ,3), 9)
            self.assertEqual(rectangle.area(0 , 10), 0)
            self.assertEqual(rectangle.area(-2.5 , 2.5), 0)
            with self.assertRaises(TypeError):
                rectangle.area("string")      

        def test_rectangle_perimeter(self):
            self.assertEqual(rectangle.perimeter(4 , 5 ), 18)
            self.assertEqual(rectangle.perimeter(0 , 0), 0)
            self.assertEqual(rectangle.perimeter(-10 , 10), 0)
            with self.assertRaises(TypeError):
                rectangle.perimeter("string")

        '''circle'''
        def test_circle_area(self):
            self.assertEqual(circle.area(3), math.pi * 3 * 3)
            self.assertEqual(circle.area(0), 0)
            self.assertEqual(circle.area(-2.5), 0)
            with self.assertRaises(TypeError):
                circle.area("string")

        def test_circle_perimeter(self):
            self.assertEqual(circle.perimeter(4), 2 * math.pi * 4)
            self.assertEqual(circle.perimeter(0), 0)
            self.assertEqual(circle.perimeter(-10),0)
            with self.assertRaises(TypeError):
                circle.perimeter("string")

def run_tests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGeometryFunctions)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    successful_tests = total_tests - failed_tests
    success_rate = (successful_tests / total_tests) * 100 if total_tests > 0 else 0

    print("\n" + "=" * 40)

    print(f"Total tests run: {total_tests}")
    print(f"Successful tests: {successful_tests}")
    print(f"Failed tests: {failed_tests}")
    print(f"Success rate: {success_rate:.2f}%")

    print("=" * 40)

if __name__ == "__main__":
        run_tests()