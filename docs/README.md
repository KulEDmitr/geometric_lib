# Math formulas
**Geometric_lib allows to use following math formulas in Python:**
## Area

- Circle: S = πR²

- Rectangle: S = ab

- Square: S = a²

- Triangle: S = ah²

  

## Perimeter

- Circle: P = 2πR

- Rectangle: P = 2a + 2b

- Square: P = 4a

- Triangle: P = a + b + c



# Functions of math formulas

## Circle
### Area
Takes circle radius value, returns circle area value.
```
def  area(r):
	return math.pi * r * r
```
***Example of function call:***
```
area(3)
28.274333882308138
```

### Perimeter
Takes circle radius value, returns circuit value.
```
def  perimeter(r):
	return  2  * math.pi * r
```
***Example of function call:***
```
perimeter(3)
18.84955592153876
```

## Rectangle
### Area
Takes rectangle sides length, returns value of rectangle area.
```
def  area(a, b):
	return a * b
```
***Example of function call:***
```
area(2, 3)
6
```

### Perimeter
Takes rectangle sides length, returns value of rectangle perimeter.
```
def  perimeter(a, b):
	return  2  * (a + b)
```
***Example of function call:***
```
perimeter(2, 5)
14
```


## Square
### Area
Takes square side length, returns value of square area.
```
def  area(a):
	return a * a
```
***Example of function call:***
```
area(4)
16
```

### Perimeter
Takes square side length, returns value of square perimeter.
```
def  perimeter(a):
	return  4  * a
```
***Example of function call:***
```
perimeter(3)
12
```


## Triangle
### Area
Takes lengths of the triangle side and triangle height, returns area of the triangle.
```
def  area(a, h):
	return a * h / 2
```
***Example of function call:***
```
area(3, 4)
6
```

### Perimeter
Takes lengths of the triangle sides, returns perimeter of the triangle.
```
def  perimeter(a, b, c):
	return a + b + c
```
***Example of function call:***
```
perimeter(3, 2, 5)
10
```


# History of project changes

**Commit** ***[a789aa9941a5de78197017f271e52e7b8f181ba6](https://github.com/kseni-sch/geometric_lib/commit/a789aa9941a5de78197017f271e52e7b8f181ba6):***
```
Author: kseni-sch <468150@niuitmo.ru>
Date: Wed Sep 25 11:23:08 2024 +0300

	Added file rectangle.py
```

**Commit** ***[d09b839b6f1d79bdf6c7b3325e9a93b894737ed5](https://github.com/kseni-sch/geometric_lib/commit/d09b839b6f1d79bdf6c7b3325e9a93b894737ed5):***
```
Author: kseni-sch <468150@niuitmo.ru>
Date: Wed Sep 25 11:45:11 2024 +0300

	Fixed file rectangle.py and added file triangle.py
```

**Commit** ***[1a5ecc8be2ec4ad5edb9bb5a76af61415e2e42e5](https://github.com/kseni-sch/geometric_lib/commit/1a5ecc8be2ec4ad5edb9bb5a76af61415e2e42e5):***
```
Author: kseni-sch <468150@niuitmo.ru>
Date:   Tue Nov 5 02:10:03 2024 +0300

    Created tests for all functions
```