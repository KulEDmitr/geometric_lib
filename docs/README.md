# Math formulas

A library for calculation geometric properties of shapes

## Functions description

### Cirсle
```python
from circle import area, perimeter
```

- area(1)          # Returns area of a circle with radius 1
    - Result: 3.1416

- perimeter(1)     # Returns perimeter of a circle with radius 1
    - Result: 6.2832

### Rectangle
```python
from rectangle import area, perimeter
```

- area(1, 1)       # Returns area of a rectangle with length 1 and width 1
    - Result: 1

- perimeter(1, 1)  # Returns perimeter of a rectangle with length 1 and width 1
    - Result: 4


### Square
```python
from square import area, perimeter
```

- area(1)          # Returns area of a square with side length 1
    - Result: 1

- perimeter(1)     # Returns perimeter of a square with side length 1
    - Result: 4


### Triangle
```python
from triangle import area, perimeter
```

- area(1, 1)         # Returns area of a triangle with base 1 and height 1
    - Result: 0.5

- perimeter(1, 1, 1) # Returns perimeter of an equilateral triangle with side lengths 1
    - Result: 3
 
## Formula Breakdown

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c\

## Development Log

### Commit hash "8ba9aeb"

    - Added circle.py
    - Added rectangle.py

### Commit hash "d078c8d"

    - Added docs

### Commit hash "071cf61"

    - Added new file (rectangle.py)

### Commit hash "936678c"

    - Fixed fault in perimeter func in file rectangle.py