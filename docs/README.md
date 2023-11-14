# Math formulas

В данном проекте содержатся 4 python файла:
- triangle.py
- circle.py
- rectangle.py
- square.py
В каждом из них находятся по две функции, которые высчитывают площадь и периметр соответствующей фигуры. 

## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah / 2 

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## Functions

- ### triangle.py

    - #### area(a, h)
    Получает на вход длину стороны треугольника и длину высоты, проведенной к этой стороне,
    и возвращает площадь треугольника
    ```
    print(area(5, 12))  =>  30

    print(area(7, 4))  =>  14
    ```

    - #### perimetr(a, b, c)
    Получает на вход длины всех сторон треугольника и выводит его периметр
    ```
    print(perimetr(5, 8, 6))  =>  19

    print(perimetr(10, 9, 8))  =>  27
    ```

- ### square.py

    - #### area(a)
    Получает на вход длину стороны квадрата и возвращает его площадь
    ```
    print(area(30))  =>  900

    print(area(7))  =>  49
    ```

    - #### perimetr(a)
    Получает на вход длину стороны квадрата и выводит его периметр
    ```
    print(perimetr(10))  =>  40

    print(perimetr(5))  =>  20
    ```

- ### rectangle.py

    - #### area(a, b)
    Принимает на вход длины двух смежных сторон прямоугольника и выводит eгo площадь
    ```
    print(area(3, 9))  =>  27

    print(area(10, 12))  => 120
    ```

    - #### perimetr(a, b)
    Принимает на вход длины двух смежных сторон прямоугольника и выводит eгo периметр
    ```
    print(perimetr(3, 9))  =>  24

    print(perimetr(10, 12))  =>  44
    ```

- ### circle.py

    - #### area(r)
    Получает на вход радиус окружности и выводит её площадь
    ```
    print(area(7))  =>  153.93804002589985

    print(area(10))  =>  314.1592653589793
    ```

    - #### perimetr(r)
    Получает на вход радиус окружности и возвращает её периметр
    ```
    print(perimetr(10))  =>  62.83185307179586

    print(perimetr(4))  =>  25.132741228718345
    ```

## Unit tests
Для проверки корректности работы вышеприведенных программ были созданы unt тесты. Они находятся в папке tests:
- rectangletests.py
- triangletests.py
- circletests.py
- squaretests.py

В каждом из файлов находятся тесты, которые проверяют:
- Правильно ли ведут себя функции при некорректных типе переданных аргументов
- Правильно ли ведут себя функции при отрицательных входных данных
- Правильно ли ведут себя функции при нулевом значении переданных аргументов

## Project history

* **c1d7b61** new addded file triangle.py and fixed bug in rectangle.py
* **91e4ed5** new added file rectangle.py
* **d078c8d** L-03: Docs added
* **8ba9aeb** L-03: Circle and square added


