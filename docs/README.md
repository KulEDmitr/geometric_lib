# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Solution Description
- Functions were made that count the area and perimeter for shapes: circle, square, rectangle and triangle.

# Description of functions
## Circle
### def area(r)
- Takes the number r, returns the area of a circle with radius r 
- r = 6:
  - return πr² = 113,097336
### def perimeter(r)
- Takes the number r, returns the perimeter of a circle with radius r
- r = 6:
    - return 2πr = 37,6991118

## Square
### def area(r)
- Takes the number a, returns the area of a square with sides a
- a = 6:
    - return a² = 36
### def perimeter(r)
- Takes the number a, returns the perimeter of a square with sides a
- a = 6:
    - return 4a = 24

## Rectangle 
### def area(r)
- Takes the numbers a and b, returns the area of a rectangle with sides a and b
- a = 6, b = 10:
    - return ab = 60
### def perimeter(r)
- Takes the numbers a and b, returns the perimeter of a rectangle with sides a and b
- a = 6, b = 10:
    - return 2(a + b) = 32

## Triangle
### def area(r)
- Takes the numbers a and h, returns the area of a triangle with side a and height h
- a = 6, h = 10:
    - return ah/2 = 30
### def perimeter(r)
- Takes the numbers a, b and c, returns the perimeter of a triangle with sides a, b and c
- a = 6, b = 8, c = 10:
    - return a + b + c = 24

# Project modification history
- commit 96d63847eb7d8c3c221deb3707a08a5d5d8e96c6 
  - Created a new branch new_features_413019
  - Added a new file rectangle.py
  

- commit 26801f878d5ed49b99a64f112f867b87239465ef 
  -  Added a new file triangle.py
  - Fixed file rectangle.py