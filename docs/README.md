# Library description
Geomitric_lib is a library for calculating the area and perimeter of different geometric figures (circles, triangles, rectangles).

---

# Figures

## Circle
- [Open in IDE](./circle.py)
- [Open on GitHub](https://github.com/HuntedDuck/geometric_lib/blob/new_features_%3C465483/circle.py)

### Parameters
- **int r**: size of circle radius  

### Functions
- `area(r)`: return area of the circle with given radius  
    **Example:**
    ```python
    from circle import area
    print(area(5))  # Output: 78.5398 (assuming π=3.14159)
    ```
- `perimeter(r)`: return perimeter of the circle with given radius  
    **Example:**
    ```python
    from circle import perimeter
    print(perimeter(5))  # Output: 31.4159 (assuming π=3.14159)
    ```

---

## Rectangle
- [Open in IDE](./rectangle.py)
- [Open on GitHub](https://github.com/HuntedDuck/geometric_lib/blob/new_features_%3C465483/rectangle.py)

### Parameters
- **int a, b**: size of rectangle sides  

### Functions
- `area(a, b)`: return area of the rectangle with given sides  
    **Example:**
    ```python
    from rectangle import area
    print(area(5, 3))  # Output: 15
    ```
- `perimeter(a, b)`: return perimeter of the rectangle with given sides  
    **Example:**
    ```python
    from rectangle import perimeter
    print(perimeter(5, 3))  # Output: 16
    ```

---

## Square
- [Open in IDE](./square.py)
- [Open on GitHub](https://github.com/HuntedDuck/geometric_lib/blob/new_features_%3C465483/square.py)

### Parameters
- **int a**: size of square side  

### Functions
- `area(a)`: return area of the square with given side  
    **Example:**
    ```python
    from square import area
    print(area(4))  # Output: 16
    ```
- `perimeter(a)`: return perimeter of the square with given side  
    **Example:**
    ```python
    from square import perimeter
    print(perimeter(4))  # Output: 16
    ```

---

## Triangle
- [Open in IDE](./triangle.py)
- [Open on GitHub](https://github.com/HuntedDuck/geometric_lib/blob/new_features_%3C465483/triangle.py)

### Parameters
- **int a, b**: size of triangle sides  

### Functions
- `area(a, b)`: return area of the triangle with given sides  
    **Example:**
    ```python
    from triangle import area
    print(area(5, 4))  # Output: 10
    ```
- `perimeter(a, b)`: return perimeter of the triangle with given sides  
    **Example:**
    ```python
    from triangle import perimeter
    print(perimeter(3, 4))  # Output: 7
    ```

---

# Math formulas

## Area
- Circle: **S = πR²**
- Rectangle: **S = ab**
- Square: **S = a²**
- Triangle: **S = 0.5ab**

## Perimeter
- Circle: **P = 2πR**
- Rectangle: **P = 2a + 2b**
- Square: **P = 4a**
- Triangle: **P = a + b**

---

# History of commits 
- [commit 097241088df9202640ce046d79a2bcfcc85983ee](https://github.com/HuntedDuck/geometric_lib/commit/097241088df9202640ce046d79a2bcfcc85983ee)  
Author: HuntedDuck <dimka.gaev@gmail.com>  
Date:   Wed Sep 25 11:57:28 2024 +0300  

    Изменена функция поиска периметра в файле rectangle.py

- [commit fee75fd0e73cd67d01c80659350d3d5855825d42](https://github.com/HuntedDuck/geometric_lib/commit/fee75fd0e73cd67d01c80659350d3d5855825d42)  
Author: HuntedDuck <dimka.gaev@gmail.com>  
Date:   Wed Sep 25 11:52:25 2024 +0300  

    Добавлен файл: rectangle.py

- [commit 4bfbe8f29963e637f7aaabcfb2895cfe7362fa24](https://github.com/HuntedDuck/geometric_lib/commit/4bfbe8f29963e637f7aaabcfb2895cfe7362fa24)  
Author: HuntedDuck <dimka.gaev@gmail.com>  
Date:   Wed Sep 25 11:34:21 2024 +0300  

    Добавлен файл: rectangle.py

- [commit d078c8d9ee6155f3cb0e577d28d337b791de28e2](https://github.com/HuntedDuck/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:55:29 2021 +0300  

    L-03: Docs added

- [commit 8ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/HuntedDuck/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)  
Author: smartiqa <info@smartiqa.ru>  
Date:   Thu Mar 4 14:54:08 2021 +0300  

    L-03: Circle and square added