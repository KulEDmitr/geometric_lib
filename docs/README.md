
# Geometric-lib

This is a python library that allows you to quickly get needed formulas to work with geometric figures.


## Usage/Examples
**All of the funcs return area(float) and perimeter(float) of specific geometric figure**
### Square
```python
import square.area, square.perimeter from geometric_lib

# a(float): square side length
def get_square_measurements(a):
  return (square.area(a), square.perimeter(a))
```
### Rectangle
```python
import rectangle.area, rectangle.perimeter from geometric_lib

# a, b(float): rectagle sides length
def get_rectangle_measurements(a, b):
  return (rectangle.area(a, b), rectangle.perimeter(a, b))
```
### Circle
```python
import circle.area, circle.perimeter from geometric_lib

# r(float): circle radius
def get_rectangle_measurements(r):
  return (circle.area(r), circle.perimeter(r))
```
### Triangle
```python
import triangle.area, triangle.perimeter from geometric_lib

# a, b, c(float): triangle sides length
# h(float): triangle height
def get_rectangle_measurements(a, b, c, h):
  return (triangle.area(a, h), circle.perimeter(a, b, c))
```
## Update history
* 6ba42c5 Docstrings added
* 74bcc29 Add triangle.py, fix perimeter func
* 597d589 Add rectangle.py
* d078c8d L-03: Docs added
* 8ba9aeb L-03: Circle and square added
