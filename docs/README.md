## Information

>This repo contains math formulas for the areas and perimeters of : Circle, Rectangle, Square, and Triangle. 

>Moreover, There are tests that control the correctness of input/output [You can check link on commits at the end](#history-of-commits)

>In addition, I've used GitHub Actions workflow to start unix tests after every single `push`. You can see more information, [using this link](https://github.com/666mxvbee/geometric_lib/commit/e59bff88621f74baf8e0cfe8973b4f7bee78cc1c)

>Geometric figures:
1) [Area of the figures](#function-descriptionsarea)
2) [Perimeter of the figures](#function-descriptions-perimeter)

## Math formulas
- **Area**:

    - ___Circle: S = πR²___
    - ___Rectangle: S = ab___
    - ___Square: S = a²___
    - ___Triangle: S = a*h/2___

- **Perimeter**:
    - ___Circle: P = 2πR___
    - ___Rectangle: P = 2a + 2b___
    - ___Square: P = 4a___
    - ___Triangle: P = a+b+c___

## Function Descriptions(Area)

- **Triangle Area**:
    - `def area(A,H)`:
    - Принимает число A(сторону треугольника).
	- Принимает число H(высоту треугольника).
	- Возвращает площадь треугольника (сторона треугольника, умноженная на высоту пополам)
	- *Параметры*:
		- ___A(int/float)___
		- ___H(int/float)___
    - *Возвращаемое значение*:
		- ___A*H/2(int/float)___ - площадь треугольника
    - `return A*H/2` 

    - ***Example***
        - `a = 1`
        - `h = 5`
        - `area(a,h) = 5`


- **Circle Area**:
    - `def area(R)`:
    - Принимает число R (радиус круга).
    - Возвращает площадь круга (π умноженное на квадрат радиуса).
    - *Параметры*:
        - ___R (int/float)___ — радиус круга
    - *Возвращаемое значение*:
        - ___π * R² (float)___ — площадь круга
    - `return math.pi * R²`

    - ***Example***
        - `R = 10`
        - `area(R) = 314.1592653589793` 


- **Rectangle Area**:
    - `def area(a, b)`:
    - Принимает число a (длину прямоугольника).
    - Принимает число b (ширину прямоугольника).
    - Возвращает площадь прямоугольника (длина, умноженная на ширину).
    - *Параметры*:
        - ___a (int/float)___ — длина прямоугольника
        - ___b (int/float)___ — ширина прямоугольника
    - *Возвращаемое значение*:
        - ___a * b (int/float)___ — площадь прямоугольника
    - `return a * b`

    - ***Example***
        - `a = 2`
        - `b = 1`
        - `area(a,b) = 2`

- **Square Area**:
    - `def area(a)`:
    - Принимает число a (сторону квадрата).
    - Возвращает площадь квадрата.
    - *Параметры*:
        - ___a (int/float)___
    - *Возвращаемое значение*:
        - ___a² (int/float)___ - площадь квадрата.
    - `return a**2`

    - ***Example***
        - `a = 3`
        - `area(a) = 9`

## Function Descriptions (Perimeter)

- **Triangle Perimeter**:
    - `def perimeter(a, b, c)`:
    - Принимает число a (сторона треугольника).
    - Принимает число b (вторая сторона треугольника).
    - Принимает число c (третья сторона треугольника).
    - Возвращает периметр треугольника (сумма всех сторон).
    - *Параметры*:
        - ___a (int/float)___
        - ___b (int/float)___
        - ___c (int/float)___
    - *Возвращаемое значение*:
        - ___a + b + c (int/float)___ - периметр треугольника.
    - `return a + b + c`

    - ***Example***
        - `a = 1`
        - `b = 2`
        - `c = 3`
        - `perimeter(a,b,c) = 6`

- **Circle Perimeter**:
    - `def perimeter(R)`:
    - Принимает число R (радиус круга).
    - Возвращает периметр круга.
    - *Параметры*:
        - ___R (int/float)___
    - *Возвращаемое значение*:
        - ___2πR (int/float)___ - периметр круга.
    - `return 2 * math.pi * R`

    - ***Example***
        - `R = 10`
        - `perimeter(R) = 62.83185307179586`

- **Rectangle Perimeter**:
    - `def perimeter(a, b)`:
    - Принимает число a (длину прямоугольника).
    - Принимает число b (ширину прямоугольника).
    - Возвращает периметр прямоугольника.
    - *Параметры*:
        - ___a (int/float)___
        - ___b (int/float)___
    - *Возвращаемое значение*:
        - ___2a + 2b (int/float)___ - периметр прямоугольника.
    - `return 2 * a + 2 * b`

    - ***Example***
        - `a = 2`
        - `b = 3`
        - `perimeter(a,b) = 10`
        

- **Square Perimeter**:
    - `def perimeter(a)`:
    - Принимает число a (сторону квадрата).
    - Возвращает периметр квадрата.
    - *Параметры*:
        - ___a (int/float)___
    - *Возвращаемое значение*:
        - ___4a (int/float)___ - периметр квадрата.
    - `return 4 * a`

    - ***Example***
        - `a = 2`
        - `perimeter(a) = 8`
        
## History of commits

- **Commit**
    - [8ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/666mxvbee/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)

    - ___L-03: Circle and square added___


- **Commit**
    - [d078c8d9ee6155f3cb0e577d28d337b791de28e2](https://github.com/666mxvbee/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)

    - ___L-03: Docs added___


- **Commit**
    - [ee4d8fb3b036550970af14d69b2364b11544db14](https://github.com/666mxvbee/geometric_lib/commit/ee4d8fb3b036550970af14d69b2364b11544db14)

    - ___был добавлен новый файл rectangle.py___


- **Commit**
    - [48ba5f8b377a40e52e4934cdf7d973ca2813fcde](https://github.com/666mxvbee/geometric_lib/commit/48ba5f8b377a40e52e4934cdf7d973ca2813fcde)

    - ___Был добавлен новый файл triangle.py. Был исправлен файл rectangle.py___

- **Commit**
    - [1d34184be77d25310e8da702ac675ef65e994f5b](https://github.com/KulEDmitr/geometric_lib/commit/1d34184be77d25310e8da702ac675ef65e994f5b)

    - ___Сделал обработку при отрицательных значений аргументов в функциях (понадобилось для будущей интеграции тестов)___

- **Commit**
    - [64b3a13986985468e69361f6bc48b7eaa8e025d1](https://github.com/KulEDmitr/geometric_lib/commit/64b3a13986985468e69361f6bc48b7eaa8e025d1)

    - ___Добавил тесты в проект (каждый файл проверяется на положительный аргумент и на значительно большой ответ, для проверки времени работы кода)___

- **Commit**
    - [e59bff88621f74baf8e0cfe8973b4f7bee78cc1c](https://github.com/666mxvbee/geometric_lib/commit/e59bff88621f74baf8e0cfe8973b4f7bee78cc1c)

    - ___Добавил `CI/CD - GitHub Actions workflow` main.yml, который запускает автоматически unit тесты, после каждой операции `push`___
