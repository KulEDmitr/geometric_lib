# Geometric Lib Python 3 Library

**[Geometric Lib](https://github.com/weizenkorn/geometric_lib)** is a _Python 3 Library_ originally created in 2021 by [smartiqa](https://github.com/smartiqaorg) and later updated in 2023 by [weizenkorn](https://github.com/weizenkorn) with the aim to ease programmers lives by giving them tools to solve some common mathematical problems.\
**The Library** is composed of 4 **Python 3** files and this Documentation, with every **Python** file dedicated to calculation of the ***area*** and ***perimeter*** of the following geometrical shapes: 
- circle
- rectangle
- square
- triangle

## Structure of the Library
- circle.py
- rectangle.py
- square.py
- triangle.py

## Contents

* ## [circle.py](../circle.py)
    `area(r)` Calculates the area of a circle by its radius `r`.\
    Next formula is being used: **S = πR<sup>2</sup>**.\
    Usage:

        area(17) = pi * 17 * 17 = 907.9202768874503

    `perimter(r)` Calculates the perimeter of a circle by its radius `r`.\
    Next formula is being used: **P = 2πR**.\
    Usage:

        perimeter(17) = 2 * pi * r = 106.81415022205297

* ## [rectangle.py](../rectangle.py)
    `area(a, b)` Calculates the area of a rectangle by its width `a` and height `b`.\
    Next formula is being used: **S = a * b**.\
    Usage:

        area(3, 4) = 3 * 4 = 12

    `perimter(a, b)` Calculates the perimeter of a rectangle by its width `a` and height `b`.\
    Next formula is being used: **P = (a + b) * 2**.\
    Usage:

        perimeter(3, 4) = (3 + 4) * 2 = 14

* ## [square.py](../square.py)
    `area(a)` Calculates the area of a square by its side `a`.\
    Next formula is being used: **S = a * a**.\
    Usage:

        area(5) = 5 * 5 = 25

    `perimter(a)` Calculates the perimeter of a square by its side `a`.\
    Next formula is being used: **P = 4 * a**.\
    Usage:

        perimeter(5) = 4 * 5 = 20

* ## [triangle.py](../triangle.py)
    `area(a, h)` Calculates the area of a triangle by its base `a` and height `h`.\
    Next formula is being used: **S = a * h / 2**.\
    Usage:

        area(10, 7) = 10 * 7 / 2 = 35

    `perimter(a, b, c)` Calculates the perimeter of a triangle by its 3 sides `a`, `b` and `c`.\
    Next formula is being used: **P = a + b + c**.\
    Usage:

        perimeter(4, 5, 6) = 4 + 5 + 6 = 15

## Commit history
**Commit history** in ***hash/message*** format, last to first. 
* **7eeeecb** | triangle.py added and rectangle.py fixed
* **71386ec** | rectangle.py
* **d078c8d** | L-03: Docs added
* **8ba9aeb** | L-03: Circle and square added