# Geometric_lib
## Description of solution
**Geometric_lib** library contains methods for counting area and perimeter of basic geometric shapes (such as circle, rectangle, square and triangle)
### Used math formulas
Methods are based on following geometric formulas:
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
## Usage examples
### Circle
Has two methods: area and perimeter, that count area and perimeter of circle accordingly, using radius.
```python
import circle
r = 5
S = circle.area(r)
P = circle.perimeter(r)
print("Area is equal to", S, "and perimeter is equal to", P) # Output: "Area is equal to 31.41592653589793 and perimeter is equal to 78.53981633974483"
```
### Rectangle
Has two methods: area and perimeter, that count area and perimeter of rectangle accordingly, using length of its two sides.
```python
import rectangle
a = 5 # Length of the first side
b = 10 # Length of the second side
S = rectangle.area(a,b)
P = rectangle.perimeter(a,b)
print("Area is equal to", S, "and perimeter is equal to", P) # Output: "Area is equal to 50 and perimeter is equal to 30"
```
### Square
Has two methods: area and perimeter, that count area and perimeter of rectangle accordingly, using length of its side.
```python
import square
a = 5 # Length of the side
S = square.area(a)
P = square.perimeter(a)
print("Area is equal to", S, "and perimeter is equal to", P) # Output: "Area is equal to 25 and perimeter is equal to 20"
```
### Triangle
Has two methods: area and perimeter, that count area and perimeter of rectangle accordingly, using length of its three sides and height.
```python
import triangle
a = 5 # Length of the first side
b = 10 # Length of the second side
c = 15 # Length of the third side
h = 10 # Length of the height
S = triangle.area(a,h)
P = triangle.perimeter(a,b,c)
print("Area is equal to", S, "and perimeter is equal to", P) # Output: "Area is equal to 50 and perimeter is equal to 30"
```
## Project commits history
1. [Added a new file rectangle.py](https://github.com/KulEDmitr/geometric_lib/tree/8be08e9febb6462e49e3589d43d5771dcab545b1) (SHA: 8be08e9febb6462e49e3589d43d5771dcab545b1). 
2. [Added triangle.py and fixed error in calculations in rectangle.py](https://github.com/KulEDmitr/geometric_lib/tree/4e22d8080aa3d4b84f352e1a5e6449888a447761) (SHA: 4e22d8080aa3d4b84f352e1a5e6449888a447761). 
3. [Actual commit of rectangle.py](https://github.com/KulEDmitr/geometric_lib/tree/6972d23beb0936ec7b5289387e9eddecd537df90) (SHA: 6972d23beb0936ec7b5289387e9eddecd537df90).