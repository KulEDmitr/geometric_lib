# Geometric library
## Description
A geometric library written using Python that contains functions to calculate area and perimeter of different geometric figures:
- Square
- Rectangle
- Triangle
- Circle

## Math formulas
### Area
- Circle: S = πR²
- Triangle: S = ah
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Triangle: P = a + b + c
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Functions 
### Circle
#### `Area(r)`
Function `area(r)` gets a number (radius) and returns a number (area value of the circle with the given radius).
```
from circle.py import area

r = 5
value_area = area(r)
print(value_area)
```
The code will print 78.53981633974483

#### `Perimeter(r)`
Function `perimeter(r)` gets a number (radius) and returns a number (perimeter value of the circle with the given radius).
```
from circle.py import perimeter

r = 5
result = perimeter(r)
print(result)
```
The code will print 31.41592653589793

### Triangle
#### `Area(a, h)`
Function `area(a, h)` gets two numbers (side of the triangle and the height to this side) and returns a number (area value of the given triangle with such side and such height).
```
from triangle.py import area

a = 3
h = 6
result = area(a, h)
print(result)
```
The code will print 9

#### `Perimeter(a, b, c)`
Function `perimeter(a, b, c)` gets three numbers (sides of the triangle) and returns a number (perimeter value of the triangle with such sides).
```
from triangle.py import perimeter

a = 3
b = 4
c = 5
result = perimeter(a, b, c)
print(result)
```
The code will print 12

### Square
#### `Area(a)`
Function `area(a)` gets a number (side of the square) and returns a number (area value of the square with such side).
```
from square.py import area

a = 5
result = area(a)
print(result)
```
The code will print 25

#### `Perimeter(a)`
Function `perimeter(a)` gets a number (side of the square) and returns a number (perimeter value of the square with such side).
```
from square.py import perimeter

a = 5
result = perimeter(a)
print(result)
```
The code will print 20

### Rectangle
#### `Area(a, b)`
Function `area(a, b)` gets two numbers (sides of the rectangle) and returns a number (area value of the given rectangle with such sides).
```
from rectangle.py import area

a = 5
b = 6
result = area(a, b)
print(result)
```
The code will print 30

#### `Perimeter(a, b)`
Function `perimeter(a, b)` gets two numbers (sides of the rectangle) and returns a number (perimeter value of the rectangle with such sides).
```
from rectangle.py import perimeter

a = 5
b = 6
result = perimeter(a, b)
print(result)
```
The code will print 22

### Changelog
Full project history
- 59e5b85342651cb93d42c3ea8e312fd2386f09a2: Fixed the error in rectangle.py
- 622f52edb84b7577ca4d136a08815d81da06847c: Added rectangle
- d078c8d9ee6155f3cb0e577d28d337b791de28e2: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460: Circle and square added
