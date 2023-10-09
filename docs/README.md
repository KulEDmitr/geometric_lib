# Geometric_lib
This project is a collection of utility functions for performing various calculations.

## Installation
To install the project, simply clone the repository.

## Functions

### Perimiter
- Circle: P = 2πR

  `def perimeter(r):

    '''Calculates the perimeter of a circle.

    circle.perimeter(3) -> 18.84955592153876'''

    return 2 * math.pi * r`
- Rectangle: P = 2a + 2b

  `def perimeter(a, b): 

    '''Calculates the perimeter of a rectangle.

    rectangle.perimeter(3, 4) -> 14'''

    return (a + b)*2`
- Square: P = 4a

  `def perimeter(a):

    '''Calculates the perimeter of a square.

    square.perimeter(4) -> 16'''

    return 4 * a`
- Triangle: P = a + b + c

  `def perimeter(a, b, c): 

    '''Calculates the perimeter of a triangle.

    triangle.perimeter(3, 4, 5) -> 12'''
    
    return a + b + c `

### Area
- Circle: S = πR²

  `def area(r):

    '''Calculate the area of a circle.

    circle.area(3) -> 28.274333882308138'''

    return math.pi * r * r`
- Rectangle: S = ab

  `def area(a, b):

    '''Calculate the area of a rectangle.

    rectangle.area(3, 4) -> 6'''

    return a * b`
- Square: S = a²

  `def area(a):

    '''Calculate the area of a square.

    square.area(3) -> 9'''

    return a * a`
- Triangle = a * h / 2

  `def area(a, h): 

    '''Calculate the area of a triangle.

    triangle.area(3, 4) -> 6'''

    return a * h / 2 `

## Commits history
- added new file (rectangle.py) - `440278a85f42e30b8e951060a2fc1e03d6c1dae1`
- added new file (triangle.py) and fix rectangle perimeter - `bc123b15d4bb47ccb74eb1bfac335a28933f92ca`
- add comments to functiond - `ca7475e9f86742c742c0f46a5e8ed693e02f936f`
- add docs - `7f5c3636b411274379311f7edc98a188705325d2`
- fix docs - `191c3edba5a07e259058b7592c2e8ce6c3e8ef52`
