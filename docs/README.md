# Math formulas
## Area
+ [Circle](#arear): S = πR²
+ [Rectangle](#areaa-b): S = ab
+ [Square](#areaa): S = a²
+ [Triangle](#areaa-h): S = ah/2

## Perimeter
+ [Circle](#perimeterr): P = 2πR
+ [Rectangle](#areaa-b): P = 2a + 2b
+ [Square](#areaa): P = 4a
+ [Triangle](#perimetera-b-c): P = a + b + c

# Discription of solution
Данная директория содержит в себе формулы для нахождения площади и периметра для следующих фигур:
+ [Circle](#circle)
+ [Rectangle](#rectangle)
+ [Square](#square)
+ [Triangle](#triangle)

# Discription of each function
## Circle
### area(r)
- Возвращает площадь круга
    - Параметры:
        - r (int): радиус круга
    - Возвращаемое значение:
        -area (float): площадь круга с радиусом r
    - Например:
        - area(5)
        - 78,539816339744830
### perimeter(r)
- Возвращает длину окружности
    - Параметры:
        - r (int): радиус круга
    - Возвращаемое значение:
        -perimeter (float): длина окружности с радиусом r
    - Например:
        - perimeter(5)
        - 31,415926535897932
## Rectangle
### area(a, b)
- Возвращает площадь прямоугольника
    - Параметры:
        - a (int): первая сторона прямоугольника
        - b (int): вторая сторона прямоугольника
    - Возвращаемое значение:
        - area (int): площадь прямоугольника со сторонам a и b
    - Например:
        - area(5, 9)
        - 45
### perimeter(a, b)
- Возвращает периметр прямоугольника
    - Параметры:
        - a (int): первая сторона прямоугольника
        - b (int): вторая сторона прямоугольника
    - Возвращаемое значение:
        -perimetr (int): периметр прямоугольника со сторонам a и b
    - Например:
        - perimeter(5, 9)
        - 28
## Square
### area(a)
- Возвращает площадь квадрата
    - Параметры:
        - a (int): сторона квадрата
    - Возвращаемое значение:
        - area (int): площадь квадрата со стороной a
    - Например:
        - area(5)
        - 25
### perimeter(a)
- Возвращает периметр квадрата
    - Параметры:
        - a (int): сторона квадрата
    - Возвращаемое значение:
        -area (int): периметр квадрата со стороной a
    - Например:
        - perimeter(5)
        - 20
## Triangle
### area(a, h)
- Возвращает площадь треугольника
    - Параметры:
        - a (int): сторона основания треугольника
        - h (int): высота треугольника
    - Возвращаемое значение:
        -area (int): площадь треугольника со стороной основания a и высотой h
    - Например:
        - area(5, 4)
        - 10
### perimeter(a, b, c)
- Возвращает периметр треугольника
    - Параметры:
        - a (int): первая сторона основания треугольника
        - b (int): вторая сторона треугольника
        - c (int): третья сторона треугольника
    - Возвращаемое значение:
        - perimeter (int): периметр треугольника со сторонами a, b и с
    - Например:
        - perimeter(5, 3, 6)
        - 21
# History of commits
- '8ba9aeb3cea847b63a91ac378a2a6db758682460' - Circle and square added
- 'd078c8d9ee6155f3cb0e577d28d337b791de28e2' - Docs added
- '97af3b266c675ebcfc3898a5c6e1a94b1fc7a8f8' -  rectangle added
- '646536406ffcb484db83d2fea4759a99dff4492b' - added triangle
- 'ccd4887055527212c551ab68fffe62bf5c9138ea' - rectangle fixed
- 'f00c50914e00027fe4819b08e1ef61c64b3fe2bd' - docs added
- '2965afa1977a4ab7743f4048c2d925ec25f1143a' - square docs added
- '10bdf746294b4f9141d6b660461cc1364ee478f6' - rectangle and triangle docs added
- '96a0ab8336843a2ef3a2c1ef99cc22eb2b0802e0' - README expanded and some files fixed