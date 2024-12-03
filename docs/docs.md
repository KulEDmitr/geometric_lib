# Geometry Library
Deffinately not a ``bicycle``

## Solution Structure.py
There is just a bunch of functions. No objects, no structure, only ***hardcore***

There is **3** files, each for one geometric shape:
* Square
* Rectangle
* Trinagle

with ```area()``` and ```perimeter()``` functions for each shape.

### Square.py
#### area(int: a) -> int: area
Parameters: a (positive int): len of the side of a square
Returns: (positive int) area of the square
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> area(3)
9
```

#### perimeter(int: a) -> int: perimeter
Parameters: a (positive int): len of the side of a square
Returns: (positive int) perimeter of the square
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> perimeter(3)
12
```

### Rectangle.py
#### area(int: a, int: b) -> int: area
Parameters: a, b (positive int): len of the sides of a rectangle
Returns: (positive int) area of the rectangle
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> area(3, 4)
12
```

#### perimeter(int: a, int: b) -> int: perimeter
Parameters: a, b (positive int): sidse of a rectangle
Returns: (positive int) perimeter of the rectangle
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> perimeter(3, 4)
14
```

### Triangle.py

#### area(int: a, int: h) -> int: area
Parameters: a (positive int): side of a triangle, h (positive int): height of a triangle
Returns: (positive int) area of the triangle
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> area(3, 4)
6
```

#### perimeter(int: a, int: b, int: c) -> int: perimeter
Parameters: a, b, c (positive int): sides of a triangle
Returns: (positive int) perimeter of the triangle
Raises: TypeErorr if value is not integer and ValueError if it's negative or zero

```
>>> perimeter(3, 4, 5)
12
```

## Testing
There is "tests" directory for your tests and test.py file with 3 basic tests classes, one for each figure
### Custom tests runner
There is "tester.py" file, which contains CustomTestResult and CustomTestRunner classes. By importing test to this file and running it you can get table of tests results with some extra data
### Now have CI/CD!
And it runs custom tester on every push on windows and ubuntu.

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

#### [Custom test runner](#custom-tests-runner)
*And also functions had been changed due to tests*
*Again*
> 18e01f1def6740abe0a23c831f14d365742b667e