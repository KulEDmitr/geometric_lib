import unittest
import circle, rectangle, square, triangle
import validation

testcases = {
    "circle": {
        "area": [
            [7, 153.93804002589986868466952578069564132566130056938018522777228502],
        ],
        "perimeter": [
            [19, 119.38052083641214306158044856462110959949243717625402119704789450],
        ]
    },
    "rectangle": {
        "area": [
            [4, 9, 36],
        ],
        "perimeter": [
            [3, 16, 38],
        ]
    },
    "square": {
        "area": [
            [3, 9],
        ],
        "perimeter": [
            [7, 28],
        ]
    },
    "triangle": {
        "area": [
            [6, 14, 42],
        ],
        "perimeter": [
            [2, 4, 5, 11],
        ]
    }
}

class ClassTestGeometricLib(unittest.TestCase):
    def setUp(self):
        self.testcases = testcases
    
    def test_circle(self):
        # test area
        for case in self.testcases["circle"]["area"]:
            self.assertAlmostEqual(
                circle.area(case[0]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            circle.area(-40)

        with self.assertRaises(validation.NotANumberException):
            circle.area("40")

        # test perimeter
        for case in self.testcases["circle"]["perimeter"]:
            self.assertAlmostEqual(
                circle.perimeter(case[0]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            circle.perimeter(-4)

        with self.assertRaises(validation.NotANumberException):
            circle.perimeter("400")

    def test_rectangle(self):
        # test_area
        for case in self.testcases["rectangle"]["area"]:
            self.assertAlmostEqual(
                rectangle.area(case[0], case[1]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            rectangle.area(10, -4)

        with self.assertRaises(validation.NotANumberException):
            rectangle.area(9, "400")

        # test_perimeter
        for case in self.testcases["rectangle"]["perimeter"]:
            self.assertAlmostEqual(
                rectangle.perimeter(case[0], case[1]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            rectangle.perimeter(8, -4)

        with self.assertRaises(validation.NotANumberException):
            rectangle.perimeter(3, "400")

    def test_square(self):
        # test_area
        for case in self.testcases["square"]["area"]:
            self.assertAlmostEqual(
                square.area(case[0]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            square.area(-4)

        with self.assertRaises(validation.NotANumberException):
            square.area("400")

        # test_perimeter
        for case in self.testcases["square"]["perimeter"]:
            self.assertAlmostEqual(
                square.perimeter(case[0]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            square.perimeter(-4)

        with self.assertRaises(validation.NotANumberException):
            square.perimeter("400")

    def test_triangle(self):
        # test_area
        for case in self.testcases["triangle"]["area"]:
            self.assertAlmostEqual(
                triangle.area(case[0], case[1]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            triangle.area(4, -9)

        with self.assertRaises(validation.NotANumberException):
            triangle.area(100, "400")

        # test_perimeter
        for case in self.testcases["triangle"]["perimeter"]:
            self.assertAlmostEqual(
                triangle.perimeter(case[0], case[1], case[2]),
                case[-1],
            )

        with self.assertRaises(validation.NonPositiveArgumentException):
            triangle.perimeter(4, -9, 8)

        with self.assertRaises(validation.NotANumberException):
            triangle.perimeter(100, "400", 99)

if __name__ == '__main__':
    unittest.main()