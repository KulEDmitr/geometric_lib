# Geometry Library
Deffinately not a ``bicycle``

## Solution Structure

There is just a bunch of functions. No objects, no structure, no types restriction, only ***hardcore***

There is **3** files, each for one geometric shape with ```area()``` and ```perimeter()``` functions for each of them:
* Square
* Rectangle
* Trinagle

### Square.py

#### Area(int: a) -> int: area
Parameters: a (int): len of the side of a square
Returns: (int) area of the square

#### Perimeter(int: a) -> int: perimeter
Parameters: a (int): len of the side of a square
Returns: (int) perimeter of the square

### Rectangle.py

#### Area(int: a, int: b) -> int: area
Parameters: a, b (int): len of the sides of a rectangle
Returns: (int) area of the rectangle

#### Perimeter(int: a, int: b) -> int: perimeter
Parameters: a, b (int): sidse of a rectangle
Returns: (int) perimeter of the rectangle

### Triangle.py

#### Area(int: a, int: h) -> int: area
Parameters: a (int): side of a triangle, h (int): height of a triangle
Returns: (int) area of the triangle

#### Perimeter(int: a, int: b, int: c) -> int: perimeter
Parameters: a, b, c (int): sides of a triangle
Returns: (int) perimeter of the triangle

## History of changes
#### Error in rectangle has been fixed
*It works fine now*
> commit 0e134b811d1074c917fdd10df4ae34a1deabc243

#### Triangle logic has been added
> commit 614d6840bec8a8650737969e9c42b4bb382a7d3d

#### Rectangle has been added:
> commit d078c8d9ee6155f3cb0e577d28d337b791de28e2