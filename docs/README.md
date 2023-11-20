# Python geometric library
The geometric library is a comprehensive collection of functions that perform calculations for various geometric shapes. The library includes functions for calculating the areas and perimeters of triangles, circles, rectangles, and squares. 

- For triangles, the library provides functions to compute the area using the multiplication of base and height divided by two. The perimeter can be calculated by summing the lengths of the sides.
- Circles are supported with functions to calculate the area using the radius multiplied by self and then to Pi and the perimeter (circumference) using 2 times pi times the radius.
- Rectangles are handled by functions that compute the area by multiplying the side lengths and the perimeter by multiplication of added side lengths and two.
- Squares can have their area calculated using one side length multiplied by self and perimeter using one side length multiplied by four.

## How to use
### Circle
#### Area
Calculate the area of a circle given its radius.

Parameters:

r (float): The radius of the circle.

Returns:

float: The calculated area of the circle.
    
Usage example:

```python
from circle import area

radius = 2.5
circle_area = area(radius)
print(f"The area of a circle with radius {radius} is: {circle_area}")
```
Output:

The area of a circle with radius 2.5 is: 19.634954084936208

#### Perimeter
Calculate the perimeter (circumference) of a circle given its radius.

Parameters:

r (float): The radius of the circle.

Returns:

float: The calculated perimeter of the circle.
    
Usage example:

```python
from circle import perimeter

radius = 3.5
circle_perimeter = perimeter(radius)
print(f"The perimeter of a circle with radius {radius} is: {circle_perimeter}")
```
Output:

The perimeter of a circle with radius 3.5 is: 21.991148575128552

### Rectangle
#### Area
Calculate the area of a rectangle given its sides.
    
Parameters:

a (float): The length of one side of the rectangle.

b (float): The length of the other side of the rectangle.
    
Returns:

float: The calculated area of the rectangle.
    
Usage example:

```python
from rectangle import area

side_a = 4.5
side_b = 2.7
rectangle_area = area(side_a, side_b)
print(f"The area of a rectangle with sides {side_a} and {side_b} is: {rectangle_area}")
```
Output:

The area of a rectangle with sides 4.5 and 2.7 is: 12.15

#### Perimeter
Calculate the perimeter of a rectangle given its sides.
    
Parameters:

a (float): The length of one side of the rectangle.

b (float): The length of the other side of the rectangle.
    
Returns:

float: The calculated perimeter of the rectangle.
    
Usage example:

```python
from rectangle import perimeter

side_a = 4.5
side_b = 2.7
rectangle_perimeter = perimeter(side_a, side_b)
print(f"The perimeter of a rectangle with sides {side_a} and {side_b} is: {rectangle_perimeter}")
```
Output:

The perimeter of a rectangle with sides 4.5 and 2.7 is: 14.4

### Square
#### Area
Calculate the area of a square given its side.
    
Parameters:

a (float): The length of a side of the square.
    
Returns:

float: The calculated area of the square.
    
Usage example:

```python
from square import area

side_a = 2.5
square_area = area(side_a)
print(f"The area of a square with side {side_a} is: {square_area}")
```
Output:

The area of a square with side 2.5 is: 6.25

#### Perimeter
Calculate the perimeter of a square given its side.
    
Parameters:

a (float): The length of a side of the square.
    
Returns:

float: The calculated perimeter of the square.
    
Usage example:

```python
from square import perimeter

side_a = 2.5
square_perimeter = perimeter(side_a)
print(f"The perimeter of a square with side {side_a} is: {square_perimeter}")
```
Output:

The perimeter of a square with side 2.5 is: 10.0

### Trinagle
#### Area
Calculate the area of a triangle given its base and height.

Parameters:

a (float): The base length of the triangle.

h (float): The height of the triangle.

Returns:

float: The calculated area of the triangle.
    
Usage example:

```python
from triangle import area

base = 4.5
height = 2.7
triangle_area = area(base, height)
print(f"The area of a triangle with base {base} and height {height} is: {triangle_area}")
```
Output:

The area of a triangle with base 4.5 and height 2.7 is: 6.075

#### Perimeter
Calculate the perimeter of a triangle given its three side lengths.

Parameters:

a (float): The length of side 'a' of the triangle.

b (float): The length of side 'b' of the triangle.

c (float): The length of side 'c' of the triangle.

Returns:

float: The calculated perimeter of the triangle.
    
Usage example:

```python
from triangle import perimeter

side_a = 4.5
side_b = 2.7
side_c = 3.8
triangle_perimeter = perimeter(side_a, side_b, side_c)
print(f"The perimeter of a triangle with sides {side_a}, {side_b}, and {side_c} is: {triangle_perimeter}")
```
Output:

The perimeter of a triangle with sides 4.5, 2.7, and 3.8 is: 11.0

## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Traingle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Testing

All modules tested with unittest, you cand find tests in [tests](./../tests) directory.

## Commit history
- 60368fc50d4082dca71beb2a891022b84e1bd6bc - bialger: Fixed comments in all .py files
- 090747fb4061055c4e297d27af929380cde8e582 - bialger: Fixed README - with usage examples
- 793f35fdf97a889f9a49b82cee54e225d4368a40 - bialger: Fixed README
- a5688e6c973e4806c9e9f61ed6f8dd34ee5c08a2 - bialger: Updated README with documentation
- f995529ccc73521d3cfb3321e1c10f23aa54a0bb - bialger: Fixed comments in triangle.py
- 880662baed38c6646f73ef3536f9b4a439bd2453 - bialger: Added comments to triangle.py
- b7c0c5e4b483deafa9dca713d4db72275083b41c - bialger: Added comments to square.py
- 52fa93ed78065fd4e769c2f8c350a5c5e4445453 - bialger: Fixed comments to rectangle.py
- 95d11a85c974e6b199f5c202def9c24ae4d30ab2 - bialger: Added comments to rectangle.py
- 29d40341f9c650a697ebd1576d35f822a592eb87 - bialger: Added comments to cirle.py
- e0203ac56eb0d8541d4e563f0d5be16d4544329c - bialger: Fixed first file
- d2d38f4176ee30484dc7250968c8e75d26029090 - bialger: Added second file
- 88729ccf10e2f6f1c4bc69b193aefa4dfb12732a - bialger: Added first file
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 - smartiqa: L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 - smartiqa: L-03: Circle and square added
