# Greetings
- Hi! This is .py files for calculating the area and perimeter of some geometric shapes. You can find out more further!

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a * h) / 2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
## Circle
### Area: area(r)
- Takes parameter r - the radius of the circle
- Return area of the circle
- Example: 
```
a = 1
b = area(a)
print(b) # 3,1415...
```
### Perimeter: perimeter(r)
- Takes parameter r - the radius of the circle
- Return circumference length
- Example:
```
a = 1
b = perimeter(a)
print(b) # 6,282...
```
## Rectangle
### Area: area(a, b)
- Takes parameters a, b - the length and width of rectangle
- Return area of the rectangle
- Example: 
```
a = 1
b = 2
c = area(a, b)
print(c) # 2
```
### Perimeter: perimeter(a, b)
- Takes parameters a, b - the length and width of rectangle
- Return perimeter of rectangle
- Example:
```
a = 1
b = 2
c = perimeter(a, b)
print(c) # 6
```

## Square
### Area: area(a)
- Takes parameter a - the length of the side of the square
- Return area of the square
- Example: 
```
a = 2
b = area(a)
print(b) # 4 
```
### Perimeter: perimeter(a)
- Takes parameter r - the length of the side of the square
- Return perimeter of the square
- Example:
```
a = 1
b = perimeter(a)
print(b) # 4
```

## Triangle
### Area: area(a, h)
- Takes parameters a, h - the length of the side of the triangle and the length of the height drawn to it
- Return area of the triangle
- Example: 
```
a = 4
h = 3
c = area(a, h)
print(c) # 6
```
### Perimeter: perimeter(a, b, c)
- Takes parameters a, b, c - the lengths of all 3 sides of the triangle
- Return perimeter of triangle
- Example:
```
a = 2
b = 2
c = 3
d = perimeter(a, b, c)
print(d) # 7
```

# Tests
- In the repository were added tests for all our geometric shapes. They marks in repo as "shape"\_tests. We are planning to add som new features cause the results. Stay tuned!

# Important commits
- d125c41eea9e8c058f07f4cbbf282cd58afb5d22 tests added
- 8dd15df5c12325b9a5d860d223b268220ac8d149 tringle added and rectangle fixed
- 411aefeb21ed72c4e393f4f32ea1c56ba8a179b6 rectangle added
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 Circle and square added
