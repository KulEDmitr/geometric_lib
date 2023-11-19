# Geometric_lib
This project is a collection of utility functions for performing various calculations.

## Installation
To install the project, simply clone the repository.

## Functions

### Perimiter
- Circle: P = 2πR

  ```py
  def perimeter(r):
    '''Calculates the perimeter of a circle.
    circle.perimeter(3) -> 18.84955592153876'''
    return 2 * math.pi * r
    ```
- Rectangle: P = 2a + 2b

  ```py
  def perimeter(a, b): 
    '''Calculates the perimeter of a rectangle.
    rectangle.perimeter(3, 4) -> 14'''
    return (a + b)*2
    ```
- Square: P = 4a

  ```py
  def perimeter(a):
    '''Calculates the perimeter of a square.
    square.perimeter(4) -> 16'''
    return 4 * a
    ```
- Triangle: P = a + b + c

  ```py
  def perimeter(a, b, c): 
    '''Calculates the perimeter of a triangle.
    triangle.perimeter(3, 4, 5) -> 12'''
    return a + b + c
     ```

### Area
- Circle: S = πR²

  ```py
  def area(r):
    '''Calculate the area of a circle.
    circle.area(3) -> 28.274333882308138'''
    return math.pi * r * r
    ```
- Rectangle: S = ab

  ```py
  def area(a, b):
    '''Calculate the area of a rectangle.
    rectangle.area(3, 4) -> 6'''
    return a * b
    ```
- Square: S = a²

  ```py
  def area(a):
    '''Calculate the area of a square.
    square.area(3) -> 9'''
    return a * a
    ```
- Triangle = a * h / 2

  ```py
  def area(a, h): 
    '''Calculate the area of a triangle.
    triangle.area(3, 4) -> 6'''
    return a * h / 2 
    ```

## Commits history
- added new file (rectangle.py) - `440278a85f42e30b8e951060a2fc1e03d6c1dae1`
- added new file (triangle.py) and fix rectangle perimeter - `bc123b15d4bb47ccb74eb1bfac335a28933f92ca`
- add comments to functiond - `ca7475e9f86742c742c0f46a5e8ed693e02f936f`
- add docs - `7f5c3636b411274379311f7edc98a188705325d2`
- fix docs - `191c3edba5a07e259058b7592c2e8ce6c3e8ef52`
- add commit history - `2b74300da88981087e30082e7b4809f8bf44b9ff`
- Update README.md - `635c552d04fddff36727ab94a6b38c870e58e972`

## UnitTests
### Circle

```py
import unittest
from circle import area,perimeter

class CircleTestCase(unittest.TestCase):
    def test_circle_area_yes(self):
        res = area(4)
        self.assertEqual(res, 50.26548245743669)

    def test_circle_area_no(self):
        res = area(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_area_real_numbers(self):
        res = area(4.25)
        self.assertEqual(res, 56.745017305465645)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_yes(self):
        res = perimeter(4)
        self.assertEqual(res, 25.132741228718345)

    def test_circle_perimeter_no(self):
        res = perimeter(-4)
        self.assertEqual(res, 'Radius cannot be negative')

    def test_circle_perimeter_real_numbers(self):
        res = perimeter(4.25)
        self.assertEqual(res, 26.703537555513243)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
```
### Rectangle
```py
import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_yes(self):
        res = area(4, 7)
        self.assertEqual(res, 28)

    def test_rectangle_area_no(self):
        res = area(4, -7)
        self.assertEqual(res, 'The sides of a rectangle cannot be negative')

    def test_rectangle_area_real_numbers(self):
        res = area(4.25, 7.36)
        self.assertEqual(res, 31.28)

    def test_rectangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_yes(self):
        res = perimeter(4, 7)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_no(self):
        res = perimeter(4, -7)
        self.assertEqual(res, 'The sides of a rectangle cannot be negative')

    def test_rectangle_perimeter_real_numbers(self):
        res = perimeter(4.25, 7.36)
        self.assertEqual(res, 23.22)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(4, 0)
        self.assertEqual(res, 8)

if __name__ == '__main__':
    unittest.main()
```
### Square
```py
import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_yes(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_square_area_no(self):
        res = area(-3)
        self.assertEqual(res, 'The side of a square cannot be negative')

    def test_square_area_real_numbers(self):
        res = area(3.45)
        self.assertEqual(res, 11.902500000000002)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_yes(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_perimeter_no(self):
        res = perimeter(-3)
        self.assertEqual(res,'The side of a square cannot be negative')

    def test_square_perimeter_real_numbers(self):
        res = perimeter(3.45)
        self.assertEqual(res, 13.8)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

if __name__ == '__main__':
    unittest.main()
```
### Triangle
```py
import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_yes(self):
        res = area(2, 8)
        self.assertEqual(res, 8)

    def test_triangle_area_no(self):
        res = area(2, -8)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_area_real_numbers(self):
        res = area(2.75, 8.6)
        self.assertEqual(res, 11.825)

    def test_triangle_area_zero(self):
        res = area(2, 0)
        self.assertEqual(res, 0)

    def test_triangle_perimeter_yes(self):
        res = perimeter(2, 8, 11)
        self.assertEqual(res, 21)

    def test_triangle_perimeter_no(self):
        res = perimeter(2, -8, 11)
        self.assertEqual(res, 'Base and height cannot be negative')

    def test_triangle_perimeter_real_numbers(self):
        res = perimeter(2.75, 8.6, 11)
        self.assertEqual(res, 22.35)

    def test_triangle_perimeter_zero(self):
        res = perimeter(2, 0, 8.59)
        self.assertEqual(res, 10.59)

if __name__ == '__main__':
    unittest.main()
```