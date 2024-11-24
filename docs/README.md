# General description
This library finds square and perimeter of figures

# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle S=ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle P=a+b+c

# Functions of library
## circle.py
### area(r)
Takes a number r - the radius of the circle, returns the area of ​​the circle

Call example:<br>
    area(4)<br>
    Input data: 4<br>
    Output data: 50.26548245743669
### perimetr(r)
Takes a number r - the radius of the circle, returns the perimeter of the circle

Call example:
    perimeter(4)
    Input data: 4
    Output data: 25.132741228718345

## rectangle.py
### area(a,b)
Takes numbers a, b - sides of the rectangle, returns the area of ​​the rectangle

Call example:
    area(4,5)
    Input data: 4 5
    Output data: 20
### perimetr(a,b)
Takes numbers a, b - the sides of the rectangle, returns the perimeter of the rectangle

Call example:
    perimeter(4,1)
    Input data: 4 1
    Output data: 10

## square.py
### area(a)
Takes a number a - the side of the square, returns the area of ​​the square

Call example:
    area(4)
    Input data: 4
    Output data: 16
### perimetr(a)
Takes a number a - the side of the square, returns the perimeter of the square

Call example:
    perimeter(3)
    Input data: 3
    Output data: 12

## triangle.py
### area(a, h)
Takes a number a - the side of the triangle to which the height h is dropped, returns the area of ​​the triangle

Call example:
    area(4,2)
    Input data: 4, 2
    Output data: 4
### perimetr(a, b, c)
Takes numbers a, b, c - sides of the triangle, returns the perimeter of the triangle

Call example:
    perimeter(4,5,4)
    Input data: 4, 5, 4
    Output data: 13

# Project change history
- commit ffe35d8940d1e6bee6e66c3a6584fa4a38f62fb8 (HEAD -> new_features_466737, origin/new_features_466737)
  Author: nikita <nikita.08t07@gmail.com>
  Date:   Fri Sep 20 10:52:14 2024 +0300

    fix_mistake
- commit 2b1e896d6bba9f97f9cf51578e55411afd497c8a
  Author: nikita <nikita.08t07@gmail.com>
  Date:   Fri Sep 20 10:48:29 2024 +0300

    add_new_file
- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added
- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
  Author: smartiqa <info@smartiqa.ru>
  Date:   Thu Mar 4 14:54:08 2021 +0300

# Requirements

1. circle_area: input one argument(side), return half the area of circle in double type
2. circle_perimeter: input one argument(side), return perimeter of circle  in double type
3. rectangle_area: input two arguments(sides), return area of rectangle in float type
4. rectangle_perimeter: input two arguments(sides), return perimeter of rectangle  in double type
5. square_area: input one argument(side), return area of square in float type
6. square_perimeter: input one argument(side), return perimeter of square  in double type
7. triangle_area: input two arguments(side, height), return area of triangle in float type
8. triangle_perimeter: input three arguments(sides), return perimeter of triangle  in double type
9. throw exceptions if not enough or too many arguments
10. don't handle data type overflows and negative numbers

# Tests

| TEST | Testing situation | Requirements | Case | Expected result | Actual result | Date | Verdict |
|-|-|-|-|-|-|-|-|
| TEST_CIRCLE_AREA_1 | return data type| return double | circle_area(4) | double | double | 14.11.24 | OK |
| TEST_CIRCLE_AREA_2 | return result | return half the area of circle |circle_area(5) | 12.5pi | 25pi | 14.11.24 | Failed(WA)|
| TEST_CIRCLE_AREA_3 | many arguments | throw exception | circle_area(5,52,7.232,13) | exception | exception | 14.11.24 | OK |
| TEST_CIRCLE_PERIMETER_4 | return data type | return double | circle_perimeter(1) | double | double | 14.11.24 | OK |
| TEST_CIRCLE_PERIMETER_5 | return result | return perimeter of circle | circle_perimeter(10) | 20pi | 20pi | 14.11.24 | OK |
| TEST_CIRCLE_PERIMETER_6 | many arguments | throw exception | circle_perimeter(5,52,7.232,13) | exception | exception | 14.11.24 | OK |
| TEST_RECTANGLE_AREA_7 | return data type | return float | rectangle_area(4,5) | float | int | 14.11.24 | Failed(WA) |
| TEST_RECTANGLE_AREA_8 | return result | return area of rectangle | rectangle_area(5,2) | 10 | 10 | 14.11.24 | OK |
| TEST_RECTANGLE_AREA_9 | many arguments | throw exception | rectangle_area(5,52,7.232,13) | exception | exception | 14.11.24 | OK |
| TEST_RECTANGLE_PERIMETER_10 | return data type | return double | rectangle_perimeter(1,5) | double | int | 14.11.24 | Failed(WA) |
| TEST_RECTANGLE_PERIMETER_11 | return result | return perimeter of rectangle | rectangle_perimeter(10,4) | 28 | 28 | 14.11.24 | OK |
| TEST_RECTANGLE_PERIMETER_12 | many arguments | throw exception | rectangle_perimeter(5,52,7.232,13) | exception | first argument | 14.11.24 | Failed(RE) |
| TEST_SQUARE_AREA_13 | return data type | return float | square_area(32.0f) | float | float | 14.11.24 | OK |
| TEST_SQUARE_AREA_14 | return result | return area of square | square_area(5) | 25 | 25 | 14.11.24 | OK |
| TEST_SQUARE_AREA_15 | many arguments | throw exception | square_area(5,52,7.232,13) | exception | exception | 14.11.24 | OK |
| TEST_SQUARE_PERIMETER_16 | return data type | return double | square_perimeter(2) | double | exception | 14.11.24 | Failed(RE) |
| TEST_SQUARE_PERIMETER_17 | return result | return perimeter of square | square_perimeter(10.6f) | 42.4 | 42.4 | 14.11.24 | OK |
| TEST_SQUARE_PERIMETER_18 | many arguments | throw exception | square_perimeter(5,52,7.232,13) | exception | exception | 14.11.24 | OK |
| TEST_TRIANGLE_AREA_19 | return data type | return float | triangle_area(1.5f,2.3f) | float | exception | 14.11.24 | Failed(RE) |
| TEST_TRIANGLE_AREA_20 | return result | return area of triangle | triangle_area(5.0,10.0) | 25 | 25 | 14.11.24 | OK |
| TEST_TRIANGLE_AREA_21 | only one argument | throw exception | triangle_area(5.f) | exception | exception | 14.11.24 | OK |
| TEST_TRIANGLE_PERIMETER_22 | return data type | return double | triangle_perimeter(1,2,3) | double | int | 14.11.24 | Failed(WA) |
| TEST_TRIANGLE_PERIMETER_23 | return result | return perimeter of triangle | triangle_perimeter(1,4,5) | 10 | 10 | 14.11.24 | OK |
| TEST_TRIANGLE_PERIMETER_24 | many arguments | throw exception | triangle_perimeter(999,1000.f,993) | exception | exception | 14.11.24 | OK |







