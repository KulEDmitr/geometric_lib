# Calculation of mathematical figures

### Each script describes what the function accepts and what it returns.Library for calculating the area and perimeter of geometric figures. Interaction with figures is divided into scripts.Each function takes its own minimum input data to calculate the geometry shape.

## <o>Structure project</o>
- docs
  - README
- circle
- rectangle
- square
- triangle


## <o>Mathematical formulas for calculation</o>
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ½ * a * h

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c




## <o>Circle</o>
The `circle.py` contains functions for calculating the area and perimeter of a circle by taking the radius value.

### Circle `area`
Calculates the area of a circle using the formula: S = πR²

#### Parameters
- `r` The radius of the circle.

#### Returns
- The area of the circle.

#### Example
```python
from circle import area
print(area(4))  # Output: 50.26548245743669
```

### Circle `perimeter`
Calculates the perimeter of a circle using the formula: P = 2πR

#### Parameters
- `r` The radius of the circle.

#### Returns
- The perimeter of the circle.

#### Example
```python
from circle import perimeter
print(perimeter(4))  # Output: 25.132741228718345
```




## <o>Rectangle</o>
The `rectangle.py` contains functions for calculating the area and perimeter of a rectangle by taking the lengths of the two sides

### Rectangle `area`
Calculates the area of a rectangle using the formula: S = ab

#### Parameters
- `a` The length of the first side.
- `b` The length of the second side.

#### Returns
- The area of the rectangle.

#### Example
```python
from rectangle import area
print(area(4, 5))  # Output: 20
```

### Rectangle `perimeter`
Calculates the perimeter of a rectangle using the formula: S = 2a + 2b


#### Parameters
- `a` The length of the first side.
- `b` The length of the second side.

#### Returns
- The perimeter of the rectangle.

#### Example
```python
from rectangle import perimeter
print(perimeter(4, 5))  # Output: 18
```




## <o>Square</o>
The `square.py` contains functions for calculating the area and perimeter of a square by taking the length one size

### Square `area`
Calculates the area of a square using the formula: S = a²

#### Parameters
- `a` The length of one side of the square.

#### Returns
- The area of the square.

#### Example
```python
from square import area
print(area(4))  # Output: 16
```

### Square `perimeter`
Calculates the perimeter of a square using the formula: S = 4a

#### Parameters
- `a` The length of one side of the square.

#### Returns
- The perimeter of the square.

#### Example
```python
from square import perimeter
print(perimeter(4))  # Output: 16
```






## <o>Triangle</o>
The `triangle.py` contains functions for calculating the area and perimeter of a square by taking the side and the height drawn to this side


### Triangle `area`
Calculates the area of a triangle using the formula:

where `a` is side, and `h` is the height drawn to this side

#### Parameters
- `a` The length of side
- `h` The height drawn to this side

#### Returns
- The area of the triangle.

#### Example
```python
from triangle import area
print(area(4, 5))  # Output: 10.0
```

### Triangle `perimeter`
Calculates the perimeter of a triangle by summing the lengths of its three sides: S = a + b + c


#### Parameters
- `a` The length of the first side.
- `b` The length of the second side.
- `c` The length of the third side.

#### Returns
- The perimeter of the triangle.

#### Example
```python
from triangle import perimeter
print(perimeter(3, 4, 5))  # Output: 12
```





## History change project:
- <r>main</r>
- <g>8ba9aeb</g> Circle and square added
- <g>d078c8d</g> Docs added
  - <o>new_features_467047</o>
    - <g>cafb494 </g> [add files with functions area calculation](https://github.com/KulEDmitr/geometric_lib/commit/cafb494b84e0804b2d138608396301afbfd10950)
    - <g>db6c273</g>  [adding comments in scripts](https://github.com/KulEDmitr/geometric_lib/commit/db6c273a40ccb6d4742f156f2aa7d7458bb5728b)
    - <g>b841306 </g> [change README](https://github.com/KulEDmitr/geometric_lib/commit/b84130616b1cf46f3894aacd21a0faf7130bd970)


<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>