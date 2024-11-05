# Geometry Library
Deffinately not a ``bicycle``

## Solution Structure.py
There is just a bunch of functions. No objects, no structure, no types restriction, only ***hardcore***

There is **3** files, each for one geometric shape:
* Square
* Rectangle
* Trinagle

with ```area()``` and ```perimeter()``` functions for each shape.

### Square.py
#### area(int: a) -> int: area
Parameters: a (int): len of the side of a square
Returns: (int) area of the square

```
>>> area(3)
9
```

#### perimeter(int: a) -> int: perimeter
Parameters: a (int): len of the side of a square
Returns: (int) perimeter of the square

```
>>> perimeter(3)
12
```

### Rectangle.py
#### area(int: a, int: b) -> int: area
Parameters: a, b (int): len of the sides of a rectangle
Returns: (int) area of the rectangle

```
>>> area(3, 4)
12
```

#### perimeter(int: a, int: b) -> int: perimeter
Parameters: a, b (int): sidse of a rectangle
Returns: (int) perimeter of the rectangle

```
>>> perimeter(3, 4)
14
```

### Triangle.py

#### area(int: a, int: h) -> int: area
Parameters: a (int): side of a triangle, h (int): height of a triangle
Returns: (int) area of the triangle

```
>>> area(3, 4)
6
```

#### perimeter(int: a, int: b, int: c) -> int: perimeter
Parameters: a, b, c (int): sides of a triangle
Returns: (int) perimeter of the triangle

```
>>> perimeter(3, 4, 5)
12
```

## History of changes
#### [Error in rectangle has been fixed](#rectanglepy)
*It works fine now*

Was:
```python
return a + b
```
Now:
```python
return 2 * (a + b)
```

> commit 0e134b811d1074c917fdd10df4ae34a1deabc243

#### [Triangle logic has been added](#trianglepy)
> commit 614d6840bec8a8650737969e9c42b4bb382a7d3d

#### [Rectangle has been added](#rectanglepy)
> commit d078c8d9ee6155f3cb0e577d28d337b791de28e2

#### [Tests has been added](#rectanglepy)
*And also functions had been changed due to tests*
> 72151de99f61a458e1510abd3fa05bd4c95ecf7c