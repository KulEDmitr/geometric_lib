# Main idea
## Goal
- Make project which will calculate area and perimeter of simple geometric figures[^1].
[^1]: Circle, Rectangle, Square and Triangle.

## Language
- I used Python :snake: because it's simple and minimalistic.

## Math formulas used in code
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
## Files
### **circle.py**
- I used this file to calculate circle's area and perimeter.
#### Calculating circle's area
- This function recieves radius of the circle and returns it's area.
```
def area(r):
    return math.pi * r * r

print(area(2))  \\ 12,566370614359173
print(area(4))  \\ 50,265482457436692
print(area(5))  \\ 78,539816339744831
```
#### Calculating circle's perimeter
- This function recieves radius of the circle and returns it's perimeter.
```
def perimeter(r):
    return 2 * math.pi * r

print(perimeter(2))  \\ 12,566370614359173
print(perimeter(4))  \\ 25,132741228718346
print(perimeter(5))  \\ 31,415926535897932
```

### **rectangle.py**
- I used this file to calculate rectangle's area and perimeter.
#### Calculating rectangle's area
- This function recieves length and width of the rectanle and returns it's area.
```
def area(a, b):
    return a * b

print(area(2, 3))   \\ 6
print(area(4, 1.5)) \\ 6
print(area(5, 5))   \\ 25
```
#### Calculating rectangle's perimeter
- This function recieves length and width of the rectanle and returns it's perimeter.
```
def perimeter(a, b):
    return 2 * (a + b)

print(perimeter(2, 3))   \\ 12
print(perimeter(4, 1.5)) \\ 15
print(perimeter(5, 5))   \\ 20
```

### **square.py**
- I used this file to calculate square's area and perimeter.
#### Calculating square's area
- This function recieves square's side length and returns square's area.
```
def area(a):
    return a * a

print(area(2))   \\ 4
print(area(4))   \\ 16
print(area(5))   \\ 25
```
#### Calculating square's perimeter
- This function recieves square's side length and returns square's perimeter.
```
def perimeter(a):
    return 4 * a

print(perimeter(2))   \\ 8
print(perimeter(4))   \\ 16
print(perimeter(5))   \\ 20
```

### **triangle.py**
- I used this file to calculate triangle's area and perimeter.
#### Calculating triangle's area
- This function recieves triangle's sides lengths and returns triangles's area.
```
def area(a, h):
    return a * h / 2

print(area(2, 1))    \\ 1
print(area(4, 3))    \\ 6
print(area(5, 10))   \\ 25
```
#### Calculating triangles's perimeter
- This function recieves triangle's sides lengths and returns triangles's perimeter.
```
def perimeter(a, b, c):
    return a + b + c

print(perimeter(2, 5, 4))   \\ 11
print(perimeter(4, 4, 1))   \\ 9
print(perimeter(5, 5, 3))   \\ 13
```

# Tests
- All files have test classes, made with [unittest](https://docs.python.org/3/library/unittest.html#) you can run it separetely by 
    ```
    python -m unittest <figure>/<figure>_test.py
    ```
- Or run all tests together by 
   ```
    python -m unittest all_tests.py
    ```
- This tests aren't testing all varians, they just prevent you from simple mistakes, you can use it for your versions of this project, or modify it if you need

# Project history
1. `8ba9aeb` Circle and square added
2. `d078c8d` Docs added
3. `6bd60b5` added rectangle.py
4. `bf7ed26` fixed rectangle.py and added triangle.py
5. `6e2e3f8` added comments in all files
6. `ae46853` added examples in comments
7. `e14f22d` Добавлены unit-тесты и отчёты
8. `89c37be` Updated test to run it all together


