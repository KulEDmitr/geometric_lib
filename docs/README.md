# Geometric Lib
____
The project is a library for calculating 
the area and perimeter of geometric figures
such as circle, square, rectangle and triangle.


## circle.py
____

### area(r)
Return the area of the circle.

**Args:**
- `r (int)`: circle radius.

**Example:**  
`area(5) --> 78.53981633974483`


### perimeter(r)
Return the perimeter of the circle.

**Args:**
- `r (int)`: circle radius.

**Example:**  
`perimeter(5) --> 31.41592653589793`

## rectangle.py
____

### area(a, b)
Return the area of the rectangle.

**Args:**
- `a (int)`: rectangle length.
- `b (int)`: rectangle width.

**Example:**  
`area(2, 4) --> 8`


### perimeter(a, b)
Return the perimeter of the rectangle.

**Args:**
- `a (int)`: rectangle length.
- `b (int)`: rectangle width.

**Example:**  
`perimeter(2, 4) --> 12`

## square.py
____

### area(a)
Return the area of the square.

**Args:**
- `a (int)`: square side length.

**Example:**  
`area(3) --> 9`


### perimeter(a)
Return the perimeter of the square.

**Args:**
- `a (int)`: square side length.

**Example:**  
`perimeter(3) --> 12`

## triangle.py
____

### area(a, h)
Return the area of the triangle.

**Args:**
- `a (int)`: triangle side length.
- `h (int)`: triangle altitude length. This height must be drawn to the side of length a.

**Example:**  
`area(3, 4) --> 6`


### perimeter(a, b, c)
Return the perimeter of the triangle.

**Args:**
- `a (int)`: length of first side of triangle.
- `b (int)`: length of second side of triangle.
- `c (int)`: length of third side of triangle.

**Example:**  
`perimeter(3, 4, 5) --> 12`

# History of commits
____

- `a7a4f97` **fixed rectangle.py**
- `973ba83` **added triangle.py**
- `ced14e8` **added rectangle.py**
- `d078c8d` **Docs added**
- `8ba9aeb` **Circle and square added**

# Testing
____

There are testing modules:

- **test_rectangle.py**
- **test_square.py**
- **test_triangle.py**
- **test_circle.py**

They test the appropriate modules for value matching and check the correctness of values.

As a result of the testing, it was found that in case of correct data the functions work correctly, but in case of incorrect data the function outputs incorrect values instead of outputting an error.
