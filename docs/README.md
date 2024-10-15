## Math formulas
This repo contains math formulas for the areas and perimeters of : Circle, Rectangle, Square, and Triangle. 

- **Area**:
    - Circle: S = πR²
    - Rectangle: S = ab
    - Square: S = a²
    - Triangle: S = a*h/2

- **Perimeter**:
    - Circle: P = 2πR
    - Rectangle: P = 2a + 2b
    - Square: P = 4a
    - Triangle: P = a+b+c

## Function Descriptions(Area)

- **Triangle Area**:
    - def area(A,H):
    - Принимает число A(сторону треугольника).
	- Принимает число H(высоту треугольника).
	- Возвращает площадь треугольника (сторона треугольника, умноженная на высоту пополам)
	- *Параметры*:
		- A(int/float)
		- H(int/float)
    - *Возвращаемое значение*:
		- A*H/2(int/float) - площадь треугольника
    - return A*H/2 

    - ***Example***
        - a = 1
        - h = 5
        - area(a,h) = 5


- **Circle Area**:
    - def area(R):
    - Принимает число R (радиус круга).
    - Возвращает площадь круга (π умноженное на квадрат радиуса).
    - *Параметры*:
        - R (int/float) — радиус круга
    - *Возвращаемое значение*:
        - π * R² (float) — площадь круга
    - return math.pi * R²

    - ***Example***
        - R = 10
        - area(R) = 314.1592653589793 


- **Rectangle Area**:
    - def area(a, b):
    - Принимает число a (длину прямоугольника).
    - Принимает число b (ширину прямоугольника).
    - Возвращает площадь прямоугольника (длина, умноженная на ширину).
    - *Параметры*:
        - a (int/float) — длина прямоугольника
        - b (int/float) — ширина прямоугольника
    - *Возвращаемое значение*:
        - a * b (int/float) — площадь прямоугольника
    - return a * b

    - ***Example***
        - a = 2
        - b = 1
        - area(a,b) = 2

- **Square Area**:
    - def area(a):
    - Принимает число a (сторону квадрата).
    - Возвращает площадь квадрата.
    - *Параметры*:
        - a (int/float)
    - *Возвращаемое значение*:
        - a² (int/float) - площадь квадрата.
    - return a**2

    - ***Example***
        - a = 3
        - area(a) = 9

## Function Descriptions (Perimeter)

- **Triangle Perimeter**:
    - def perimeter(a, b, c):
    - Принимает число a (сторона треугольника).
    - Принимает число b (вторая сторона треугольника).
    - Принимает число c (третья сторона треугольника).
    - Возвращает периметр треугольника (сумма всех сторон).
    - *Параметры*:
        - a (int/float)
        - b (int/float)
        - c (int/float)
    - *Возвращаемое значение*:
        - a + b + c (int/float) - периметр треугольника.
    - return a + b + c

    - ***Example***
        - a = 1
        - b = 2
        - c = 3
        - perimeter(a,b,c) = 6

- **Circle Perimeter**:
    - def perimeter(R):
    - Принимает число R (радиус круга).
    - Возвращает периметр круга.
    - *Параметры*:
        - R (int/float)
    - *Возвращаемое значение*:
        - 2πR (int/float) - периметр круга.
    - return 2 * math.pi * R

    - ***Example***
        - R = 10
        - perimeter(R) = 62.83185307179586

- **Rectangle Perimeter**:
    - def perimeter(a, b):
    - Принимает число a (длину прямоугольника).
    - Принимает число b (ширину прямоугольника).
    - Возвращает периметр прямоугольника.
    - *Параметры*:
        - a (int/float)
        - b (int/float)
    - *Возвращаемое значение*:
        - 2a + 2b (int/float) - периметр прямоугольника.
    - return 2 * a + 2 * b

    - ***Example***
        - a = 2
        - b = 3
        - perimeter(a,b) = 10
        

- **Square Perimeter**:
    - def perimeter(a):
    - Принимает число a (сторону квадрата).
    - Возвращает периметр квадрата.
    - *Параметры*:
        - a (int/float)
    - *Возвращаемое значение*:
        - 4a (int/float) - периметр квадрата.
    - return 4 * a

    - ***Example***
        - a = 2
        - perimeter(a) = 8
        
## History of commits

- **Commit**
    - 8ba9aeb3cea847b63a91ac378a2a6db758682460

    - L-03: Circle and square added


- **Commit**
    - d078c8d9ee6155f3cb0e577d28d337b791de28e2 

    - L-03: Docs added


- **Commit**
    - ee4d8fb3b036550970af14d69b2364b11544db14

    - был добавлен новый файл rectangle.py


- **Commit**
    - 48ba5f8b377a40e52e4934cdf7d973ca2813fcde 

    - Был добавлен новый файл triangle.py. Был исправлен файл rectangle.py
