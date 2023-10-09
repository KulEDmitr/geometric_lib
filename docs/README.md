# Geometric_lib
This project is a collection of utility functions for performing various calculations.

## Installation
To install the project, simply clone the repository.

## Functions

### Perimiter
- Circle: P = 2πR

  `def perimeter(r):
    return 2 * math.pi * r`
- Rectangle: P = 2a + 2b

  `def perimeter(a, b): 
    return (a + b)*2`
- Square: P = 4a

  `def perimeter(a):
    return 4 * a`
- Triangle: P = a + b + c

  `def perimeter(a, b, c): 
    return a + b + c`

### Area
- Circle: S = πR²

  `def area(r):
    return math.pi * r * r`
- Rectangle: S = ab

  `def area(a, b):
    return a * b`
- Square: S = a²

  `def area(a):
    return a * a`
- Triangle = a * h / 2

  `def area(a, h): 
    return a * h / 2`

## Commits history
- added new file (rectangle.py) - `440278a85f42e30b8e951060a2fc1e03d6c1dae1`
- added new file (triangle.py) and fix rectangle perimeter - `bc123b15d4bb47ccb74eb1bfac335a28933f92ca`
- add comments to functiond - `ca7475e9f86742c742c0f46a5e8ed693e02f936f`
- add docs - `7f5c3636b411274379311f7edc98a188705325d2`
- fix docs - `191c3edba5a07e259058b7592c2e8ce6c3e8ef52`
