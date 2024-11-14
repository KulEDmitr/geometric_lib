# `Math formulas and function call examples`

## [*Circle*](../circle.py)

- **Area**: S = πR²

- The function *CircleArea(r)* takes the radius of the circle as an argument and returns the area of the circle after applying the formula.

> **Function call example for func area(r):**
> 
> Input: 10
> 
> Output: 314.1592653589793
> 
- **Perimeter**: P = 2πR

- The function *CircleArea(r)* takes the radius of the circle as an argument and returns the perimeter of the circle after applying the formula.

> **Function call example for func perimeter(r):**
> 
> Input: 10
> 
> Output: 62.83185307179586

## [*Triangle*](../triangle.py)

- **Area**: S = a⋅h/2

- The function *TriangleArea(a, h)* takes the side and the height of the triangle as an argument and returns the area of the triangle after applying the formula.

> **Function call example:**
> 
> Input: 10 15
> 
> Output: 75.0
>
- **Perimeter**: P = a + b + c

- The function *TrianglePerimeter(a, b, c)* takes three sides of the triangle as an argument and returns the perimeter of the triangle after applying the formula.

> **Function call example:**
> 
> Input: 9 12 15
> 
> Output: 36

## [*Rectangle*](../rectangle.py)

- **Area**: S = a⋅b

- The function *RectangleArea(a, b)* takes two sides of the rectangle as an argument and returns the area of the rectangle after applying the formula.

> **Function call example:**
> 
> Input: 10 4
> 
> Output: 40
>
- **Perimeter**: P = 2a + 2b

- The function *RectanglePerimeter(a, b)* takes two sides of the rectangle as an argument and returns the perimeter of the rectangle after applying the formula.

> **Function call example:**
> 
> Input: 10 4
> 
> Output: 28

## [*Square*](../square.py)

- **Area**: S = a²

- The function *SquareArea(a)* takes the side of the square as an argument and returns the area of the square after applying the formula.

> **Function call example:**
> 
> Input: 10
> 
> Output: 100

- **Perimeter**: P = 4a

- The function *SquarePerimeter(a)* takes the side of the square as an argument and returns the perimeter of the square after applying the formula.

> **Function call example:**
> 
> Input: 10
> 
> Output: 40

# `Project change history and commit hashes`

- [`3a47939`](https://github.com/KulEDmitr/geometric_lib/commit/3a4793914923c53cb6c4cbacbad8a692b43b1b7f) Commit hashes has been changed
- [`840e11d`](https://github.com/KulEDmitr/geometric_lib/commit/840e11dc684b91ba58614e43eda68963786ec876) (HEAD -> new_features_466499) Added Project change history and commit hashes
- [`623e552`](https://github.com/KulEDmitr/geometric_lib/commit/623e5528175fa8025f3e67b1fa54f74064dd8841) Added a general description of the solution and a description of each function
- [`013ee62`](https://github.com/KulEDmitr/geometric_lib/commit/013ee6289774d5b0d8d207df40b2778deae12254) Triangle file has been changed
- [`b265fd8`](https://github.com/KulEDmitr/geometric_lib/commit/b265fd8060ebe281e102b0ff0265b9270e61b8f6) (origin/new_features_466499, geometcirc_lib) Добавлены изменения в вычисление периметра
- [`4e63f2b`](https://github.com/KulEDmitr/geometric_lib/commit/4e63f2b4da69b4d118714c7514203a487d5a46b5) Добавлен еще один файл
- [`05d3f79`](https://github.com/KulEDmitr/geometric_lib/commit/05d3f793a40a9e14f1aea910ec08ce09a124ecba) Добавлен новый файл

# `Tests`

- [`triangle_tests`](../tests/triangle_tests.py)

> function: test_triangle_area_natural_numbers(self)
> 
> >tests if program calculates area of a triangle correctly if input data is natural numbers
> 
> function: test_triangle_area_negative_numbers(self)
> 
> >tests if program for calculating the area of a triangle correctly displays an error if the input data is negative numbers
> 
> function: test_triangle_area_chars(self)
> 
> >tests if program for calculating the area of a triangle correctly displays an error if the input data is chars
>
> function: test_triangle_area_big_numbers(self)
> 
> >tests if program calculates perimeter of a triangle correctly if input data is big numbers
>
> function: test_triangle_perimeter_natural_numbers(self)
> 
> >tests if program calculates perimeter of a triangle correctly if input data is natural numbers
>
> function: test_triangle_perimeter_negative_number(self)
>
> >tests if program for calculating the perimeter of a triangle correctly displays an error if the input data is negative numbers
>
> function: test_triangle_perimeter_chars(self)
> 
> >tests if program for calculating the perimeter of a triangle correctly displays an error if the input data is chars
>
> function: test_triangle_perimeter_big_numbers(self)
> 
> >tests if program calculates perimeter of a triangle correctly if input data is big numbers

- [`circle_tests`](../tests/circle_tests.py)

> function: test_circle_area_natural_numbers(self)
> 
> >tests if program calculates area of a circle correctly if input data is natural numbers
> 
> function: test_circle_area_negative_numbers(self)
> 
> >tests if program for calculating the area of a circle correctly displays an error if the input data is negative numbers
> 
> function: test_circle_area_chars(self)
> 
> >tests if program for calculating the area of a circle correctly displays an error if the input data is chars
>
> function: test_circle_area_big_numbers(self)
> 
> >tests if program calculates perimeter of a circle correctly if input data is big numbers
>
> function: test_triangle_circle_natural_numbers(self)
> 
> >tests if program calculates perimeter of a circle correctly if input data is natural numbers
>
> function: test_circle_perimeter_negative_number(self)
>
> >tests if program for calculating the perimeter of a circle correctly displays an error if the input data is negative numbers
>
> function: test_circle_perimeter_chars(self)
> 
> >tests if program for calculating the perimeter of a circle correctly displays an error if the input data is chars
>
> function: test_circle_perimeter_big_numbers(self)
> 
> >tests if program calculates perimeter of a circle correctly if input data is big numbers

- [`square_tests`](../tests/square_tests.py)

> function: test_square_area_natural_numbers(self)
> 
> >tests if program calculates area of a square correctly if input data is natural numbers
> 
> function: test_square_area_negative_numbers(self)
> 
> >tests if program for calculating the area of a square correctly displays an error if the input data is negative numbers
> 
> function: test_square_area_chars(self)
> 
> >tests if program for calculating the area of a square correctly displays an error if the input data is chars
>
> function: test_square_area_big_numbers(self)
> 
> >tests if program calculates area of a square correctly if input data is big numbers
>
> function: test_square_perimeter_natural_numbers(self)
> 
> >tests if program calculates perimeter of a square correctly if input data is natural numbers
>
> function: test_square_perimeter_negative_number(self)
>
> >tests if program for calculating the perimeter of a square correctly displays an error if the input data is negative numbers
>
> function: test_square_perimeter_chars(self)
> 
> >tests if program for calculating the perimeter of a square correctly displays an error if the input data is chars
>
> function: test_square_perimeter_big_numbers(self)
> 
> >tests if program calculates perimeter of a square correctly if input data is big numbers

- [`rectangle_tests`](../tests/rectangle_tests.py)

> function: test_rectangle_area_natural_numbers(self)
> 
> >tests if program calculates area of a rectangle correctly if input data is natural numbers
> 
> function: test_rectangle_area_negative_numbers(self)
> 
> >tests if program for calculating the area of a rectangle correctly displays an error if the input data is negative numbers
> 
> function: test_rectangle_area_chars(self)
> 
> >tests if program for calculating the area of a rectangle correctly displays an error if the input data is chars
>
> function: test_rectangle_area_big_numbers(self)
> 
> >tests if program calculates area of a rectangle correctly if input data is big numbers
>
> function: test_rectangle_perimeter_natural_numbers(self)
> 
> >tests if program calculates perimeter of a rectangle correctly if input data is natural numbers
>
> function: test_rectangle_perimeter_negative_number(self)
>
> >tests if program for calculating the perimeter of a rectangle correctly displays an error if the input data is negative numbers
>
> function: test_rectangle_perimeter_chars(self)
> 
> >tests if program for calculating the perimeter of a rectangle correctly displays an error if the input data is chars
>
> function: test_rectangle_perimeter_big_numbers(self)
> 
> >tests if program calculates perimeter of a rectangle correctly if input data is big numbers