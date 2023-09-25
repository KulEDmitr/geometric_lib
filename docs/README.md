# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Modules
## circle
### circle.area(r)
```python
area(r: int) -> int
    Gets radius of circle, returns area
```
Example
```python
>>> circle.area(2)
12.566370614359172
```

### circle.perimeter(r)
```python
perimeter(r: int) -> int
    Gets perimeter of circle, returns perimeter
```
Example
```python
>>> circle.perimeter(3)
18.84955592153876
```


## rectangle
### rectangle.area(a, b)
```python
area(a: int, b: int) -> int
    Returns area of rectangle
    
    Parameters:
            a (int): length of rectangle
            b (int): width of rectangle
    Returns:
            area (int): area of rectangle
```
Example
```python
>>> rectangle.area(1, 2)
2
```

### rectangle.perimeter(a, b)
```python
perimeter(a: int, b: int) -> int
    Returns perimeter of rectangle
    
    Parameters:
        a (int): length of rectangle
        b (int): width of rectangle
    Returns:
        perimeter (int): perimeter of rectangle
```
Example
```python
>>> rectangle.perimeter(1, 2)
6
```


## square
### square.area(a)
```python
area(a: int) -> int
    Gets side of square, returns area
```
Example
```python
>>> square.area(2)
4
```

### square.perimeter(a)
```python
perimeter(a: int) -> int
    Gets side of square, returns perimeter
```
Example
```python
>>> square.perimeter(2)
8
```


## triangle
### triangle.area(a, h)
```python
area(a: int, h: int) -> float
    Returns area of triangle
    
    Parameters:
            a (int): one side of triangle
            h (int): height to given side of triangle
    Returns:
            area (float): area of rectangle
```
Example
```python
>>> triangle.area(2, 3)
3.0
```

### triangle.perimeter(a, b, c)
```python
perimeter(a: int, b: int, c: int) -> int
    Returns perimeter of triangle
    
    Parameters:
            a (int): first side of triangle
            b (int): second side of triangle
            c (int): third side of triangle
    Returns:
            perimeter (int): perimeter of triangle
```
Example
```python
>>> triangle.perimeter(1, 2, 3)
6
```

# Commits
- `8ba9aeb`: L-03: Circle and square added
- `d078c8d`: L-03: Docs added
- `5580e9d`: added rectangle.py
- `9abb177`: added triangle.py
- `20b0f05`: fixed perimeter in rectangle.py