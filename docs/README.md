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

## Contents
There are 4 unittest files the initial 4 python executable files composing the libary. Their prefix is "test_". Every file contains 3 tests for every of the functions. The tests are: test_x_basic, test_x_invalid_value, test_x_invalid_type.

## Commit history
**Commit history** in ***hash/message*** format, last to first. 
* **[7eeeecb](https://github.com/KulEDmitr/geometric_lib/commit/7eeeecbf58663a811086ff3c56efc6d3d506075e)** | triangle.py added and rectangle.py fixed
* **[71386ec](https://github.com/KulEDmitr/geometric_lib/commit/71386ecd8497795a605ea098730d7afecf81fc75)** | rectangle.py
* **[d078c8d](https://github.com/smartiqaorg/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)** | L-03: Docs added
* **[8ba9aeb](https://github.com/smartiqaorg/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)** | L-03: Circle and square added
* **[8b1afe5](https://github.com/KulEDmitr/geometric_lib/commit/8b1afe5f18a9ba86ff92894026586df0544247e5)** | unittests added